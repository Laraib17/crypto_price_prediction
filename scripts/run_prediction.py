from collections import OrderedDict
import argparse
import os
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
class predictor:
    def __init__(self, model, device):
        self.model = model.to(device)
        self.device = device

    def predict(self, dataloader):
        self.model.eval()
        predictions = []
        with torch.no_grad():
            for inputs in dataloader:
                inputs = inputs.to(self.device)
                outputs = self.model(inputs)
                _, preds = torch.max(outputs, 1)
                predictions.extend(preds.cpu().numpy())
        return predictions