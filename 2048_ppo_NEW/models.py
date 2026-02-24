# models.py

import torch
import torch.nn as nn
import numpy as np

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Max tile we ever expect (2^17 = 131072), used for normalization
LOG2_MAX = 17.0


def log2_encode(x: torch.Tensor) -> torch.Tensor:
    """
    Map raw tile values to log2 space, normalized to [0, 1].
    Empty cells (0) stay 0. Tile 2->1/17, tile 4->2/17, ..., tile 131072->1.0
    """
    return torch.where(x > 0, torch.log2(x.clamp(min=1.0)) / LOG2_MAX, torch.zeros_like(x))


class PolicyNet(nn.Module):
    """
    Policy network for 2048.

    Dual-path architecture:
      - Spatial path: Conv2d over the 4x4 log2-encoded board
      - Flat path:    MLP over the flattened log2-encoded board

    Input:  (B, 16) raw tile values
    Output: (B, 4)  action probabilities
    """

    def __init__(self):
        super().__init__()

        # Spatial path
        self.conv = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size=2, padding=1),   # (B,64,5,5)
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=2),             # (B,128,4,4)
            nn.ReLU(),
            nn.Conv2d(128, 128, kernel_size=2),            # (B,128,3,3)
            nn.ReLU(),
            nn.Flatten(),                                  # (B, 1152)
        )

        # Flat path
        self.flat = nn.Sequential(
            nn.Linear(16, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
        )

        # Combined head
        self.head = nn.Sequential(
            nn.Linear(1152 + 256, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 4),
        )

    def forward(self, x):
        enc      = log2_encode(x)
        spatial  = enc.view(-1, 1, 4, 4)
        conv_out = self.conv(spatial)
        flat_out = self.flat(enc)
        combined = torch.cat([conv_out, flat_out], dim=1)
        return torch.softmax(self.head(combined), dim=-1)


class ValueNet(nn.Module):
    """
    Value network for 2048. Same dual-path structure as PolicyNet.

    Input:  (B, 16) raw tile values
    Output: (B, 1)  scalar state value
    """

    def __init__(self):
        super().__init__()

        self.conv = nn.Sequential(
            nn.Conv2d(1, 64, kernel_size=2, padding=1),
            nn.ReLU(),
            nn.Conv2d(64, 128, kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(128, 128, kernel_size=2),
            nn.ReLU(),
            nn.Flatten(),
        )

        self.flat = nn.Sequential(
            nn.Linear(16, 256),
            nn.ReLU(),
            nn.Linear(256, 256),
            nn.ReLU(),
        )

        self.head = nn.Sequential(
            nn.Linear(1152 + 256, 512),
            nn.ReLU(),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Linear(256, 1),
        )

    def forward(self, x):
        enc      = log2_encode(x)
        spatial  = enc.view(-1, 1, 4, 4)
        conv_out = self.conv(spatial)
        flat_out = self.flat(enc)
        combined = torch.cat([conv_out, flat_out], dim=1)
        return self.head(combined)


def encode_board(board: np.ndarray) -> torch.Tensor:
    """Convert a 4x4 numpy board to a flat float tensor (raw; networks encode internally)."""
    return torch.FloatTensor(board.flatten().astype(np.float32))
