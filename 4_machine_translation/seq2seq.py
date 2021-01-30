import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence as pack
from torch.nn.utils.rnn import pack_padded_sequence as unpack

class Attention(nn.Module):
    def __init__(self, hidden_size):
        super(Attention, self).__init__()

        self.linear = nn.Linear(hidden_size, hidden_size, bias=False)
        self.softmax = nn.Softmax(dim=-1)

    def forward(self, h_src, h_t_tgt, mask=None)
        query = self.linear(h_t_tgt)

        weight = torch.bmm(query, h_src.transpose(1, 2))
        if mask is not None:
            weight.masked_fill_(mask.unsqueeze(1), -float('inf'))
        weight = self.softmax(weight)

        context_vector = torch.bmm(weight, h_src)

        return context_vector

class Encoder(nn.Module):
    def __init__(self, word_vec_size, hidden_size, n_layers=4, dropout_p=2):
        super(Encoder, self).__init__()
        
        self.rnn = nn.LSTM(
            word_vec_size,
            int(hidden_size / 2),
            num_layers = n_layers,
            dropout = dropout_p,
            bidirectional = True,
            batch_first = True,
        )
        
    def forward(self, emb):
        if isinstance(emb, tuple):
            x, lengths = emb
            x = pack(x, lengths.tolist(), batch_first = True)
            
        else:
            x = emb
        
        y, h = self.rnn(x)
        
        if isinstance(emb, tuple):
            y, _ = unpack(y, batch_first = True)
        
        return y, h

class Decoder(nn.Module):
    def __init__(self, word_vec_size, hidden_size, n_layers=4, dropout_p=.2):
        super(Decoder, self).__init__()

        self.rnn = nn.LSTM(
            word_vec_size + hidden_size,
            hidden_size,
            num_layers=n_layers,
            dropout=dropout_p,
            bidirectional=False,
            batch_first=True,
        )

    def forward(self, emb_t, h_t_1_tilde, h_t_1):
        batch_size = emb_t.size(0)
        hidden_size = h_t_1[0].size(-1)

        if h_t_1_tilde is None:
            h_t_1_tilde = emb_t.new(batch_size, 1, hidden_size).zero_()

            x = torch.cat([emb_t, h_t_1_tilde], dim=-1)

            y, h = self.rnn(x, h_t_1)

            return y, h

class Generator(nn.Module):
    def __init__(self, hidden_size, output_size):
        super(Generator, self).__init__()

        self.output = nn.Linear(hidden_size, ouotput_size)
        self.softmax = nn.LogSoftmax(dim=-1)

    def forward(self, x):
        y = self.softmax(self.output(x))

        return y