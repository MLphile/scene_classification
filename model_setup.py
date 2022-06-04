from torchvision import models
import torch.nn as nn

model = models.resnext50_32x4d(pretrained=True)

inputs = model.fc.in_features
outputs = 6
clf = nn.Sequential(
    #               nn.Dropout(0.30),
    nn.Linear(inputs, outputs)
)

model.fc = clf
