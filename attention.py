import torch
import torch.nn as nn
import math

class SelfAttention(nn.Module):
    def __init__(self, dropout=0.1):
        super().__init__()
        self.softmax=nn.Softmax(dim=-1)
        self.dropout=nn.Dropout(dropout)
        
    def forward(self, Q, K, V, mask=None):
        d_k=Q.size(-1)
        score=torch.matmul(Q,K.transpose(-1, -2)) / math.sqrt(d_k)
        if mask is not None:
            score=score.masked_fill(mask==0, float('-inf'))
        attn=self.softmax(score)
        attn=self.dropout(attn)
        out=torch.matmul(attn, V)
        return out, attn

