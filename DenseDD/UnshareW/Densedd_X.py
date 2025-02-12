import torch
from torch import nn
from torch.nn import functional as F


class DenseddNet_X(nn.Module):

    def __init__(self):
        super(DenseddNet_X, self).__init__()

        # xw+b
        self.fc0 = nn.Linear(28*28, 256, bias=False)
        self.dd = nn.Linear(256, 256, bias=False)
        self.dd2 = nn.Linear(256, 256, bias=False)
        self.dd3 = nn.Linear(256, 256, bias=False)
        self.dd4 = nn.Linear(256, 256, bias=False)

        self.fc2 = nn.Linear(256, 10, bias=False)

    def forward(self, x):
        # x: [b, 1, 28, 28]
        x = self.fc0(x)
        c = x
        # h1 = x@w1*x
        
        g=self.dd(x)
        x=g*c+c

        g2=self.dd2(x)
        x=g2*c+c

        g3=self.dd3(x)
        x=g3*c+c

        g4=self.dd4(x)
        x=g4*c+c

        x = self.fc2(x)
        return x
