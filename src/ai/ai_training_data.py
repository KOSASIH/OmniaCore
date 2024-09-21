import numpy as np
import pandas as pd

class ElysiumDataset(Dataset):
    def __init__(self):
        # Load the training data
        self.data = pd.read_csv('training_data.csv')

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        # Get the input and output data for the current sample
        inputs = self.data.iloc[index, :-1].values
        labels = self.data.iloc[index, -1].values

        # Convert the data to PyTorch tensors
        inputs = torch.tensor(inputs, dtype=torch.float32)
        labels = torch.tensor(labels, dtype=torch.float32)

        return inputs, labels

# Example usage
dataset = ElysiumDataset()
print(len(dataset))
print(dataset[0])
