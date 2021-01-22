import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence as pack
from torch.nn.utils.rnn import pack_padded_sequence as unpack

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