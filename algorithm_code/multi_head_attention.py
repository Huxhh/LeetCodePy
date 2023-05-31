import torch
import torch.nn as nn
import torch.nn.functional as F


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super(MultiHeadAttention, self).__init__()

        # 确保模型的维度可以被头数整除
        assert d_model % num_heads == 0

        # 计算每个头的维度
        self.d_k = d_model // num_heads

        self.num_heads = num_heads
        self.d_model = d_model

        # 定义线性层
        self.W_q = nn.Linear(d_model, d_model)  # Query 线性变换
        self.W_k = nn.Linear(d_model, d_model)  # Key 线性变换
        self.W_v = nn.Linear(d_model, d_model)  # Value 线性变换

        # 最后的线性层
        self.W_o = nn.Linear(d_model, d_model)

    def forward(self, Q, K, V):
        # 获取batch_size
        batch_size = Q.size(0)

        # 线性变换
        Q = self.W_q(Q)
        K = self.W_k(K)
        V = self.W_v(V)

        # 将d_model分成多头
        Q = Q.view(batch_size, -1, self.num_heads, self.d_k)
        K = K.view(batch_size, -1, self.num_heads, self.d_k)
        V = V.view(batch_size, -1, self.num_heads, self.d_k)

        # 将头维度移到前面
        Q = Q.transpose(1, 2)
        K = K.transpose(1, 2)
        V = V.transpose(1, 2)

        # 计算score
        scores = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(self.d_k).float())

        # softmax获取权重
        attn = F.softmax(scores, dim=-1)

        # 通过权重计算新的V
        context = torch.matmul(attn, V)

        # 将多头合并
        context = context.transpose(1, 2).contiguous().view(batch_size, -1, self.d_model)

        # 通过最后的线性层
        output = self.W_o(context)

        return output, attn
