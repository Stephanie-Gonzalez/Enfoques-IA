# -*- coding: utf-8 -*-
"""
@author: sttep
"""


import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision.datasets import MNIST
from torchvision.transforms import ToTensor
from torchvision.models import resnet18

# Configuración de dispositivos
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Cargar el conjunto de datos MNIST y aplicar transformaciones
train_dataset = MNIST(root='data/', train=True, transform=ToTensor(), download=True)
test_dataset = MNIST(root='data/', train=False, transform=ToTensor())

# Crear dataloaders para el conjunto de entrenamiento y prueba
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# Definir la arquitectura del modelo
model = resnet18(num_classes=10).to(device)

# Definir la función de pérdida y el optimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenamiento del modelo
num_epochs = 10
for epoch in range(num_epochs):
    running_loss = 0.0
    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)
        
        # Calcular las salidas y la pérdida
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Retropropagación y optimización
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(train_loader):.4f}')

# Evaluación del modelo en el conjunto de prueba
model.eval()
total_correct = 0
total_samples = 0

with torch.no_grad():
    for images, labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)
        
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        
        total_samples += labels.size(0)
        total_correct += (predicted == labels).sum().item()

accuracy = total_correct / total_samples
print(f'Accuracy on test set: {accuracy:.2%}')
