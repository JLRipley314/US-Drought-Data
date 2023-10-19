import torch
import torch.nn as nn

class LSTMModel(nn.Module):
    """
    For reading in one dimensional time series data. 
    """
    def __init__(self, input_dim = 1, hidden_dim = 50, layer_dim = 1, output_dim = 1):
        super(LSTMModel, self).__init__()
        self.hidden_dim = hidden_dim
        self.layer_dim = layer_dim
        self.lstm = nn.LSTM(input_dim, hidden_dim, layer_dim, batch_first=True)
        self.linear = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()
        c0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()
        
        # We need to detach as we are doing truncated backpropagation through time (BPTT)
        # If we don't, we'll backprop all the way to the start even after going through another batch
        # We make a view to x so that it is a 3 index tensor. We assume one batch.

        out, (hn, cn) = self.lstm(x.view(len(x),1,-1), (h0.detach(), c0.detach()))
        out = self.linear(out.view(len(x),-1))
       
        # last element is the prediction from the sequence of inputs 
        return out[-1] 
