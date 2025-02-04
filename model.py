import torch
import torch.nn as nn
import pennylane as qml
import torch.nn as nn
import pennylane as qml
import torch.nn.functional as F

n_qubits = 5
dev = qml.device("default.qubit", wires=n_qubits)

@qml.qnode(dev)
def qnode(inputs, weights):
    qml.AngleEmbedding(inputs, wires=range(n_qubits)) 
    qml.StronglyEntanglingLayers(weights, wires=range(n_qubits))
    return [qml.expval(qml.PauliZ(wires=i)) for i in range(n_qubits)]

n_layers = 3
weight_shapes = {"weights": (n_layers, n_qubits, 3)}

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 5, stride=1, padding=2)
        self.bn1 = nn.BatchNorm2d(16)
        self.pool = nn.MaxPool2d(2, 2)

        self.conv2 = nn.Conv2d(16, 32, 5, stride=1, padding=2)
        self.bn2 = nn.BatchNorm2d(32)


        self.qlayer1 = qml.qnn.TorchLayer(qnode, weight_shapes)
        self.qlayer2 = qml.qnn.TorchLayer(qnode, weight_shapes)
        self.qlayer3 = qml.qnn.TorchLayer(qnode, weight_shapes)
        self.qlayer4 = qml.qnn.TorchLayer(qnode, weight_shapes)

        self.fc1 = nn.Linear(32 * 16 * 16, 120)
        self.fc2 = nn.Linear(120, 20)
        self.fc3 = nn.Linear(20, 11)

    def forward(self, x):
        x = self.pool(F.relu(self.bn1(self.conv1(x))))
        x = self.pool(F.relu(self.bn2(self.conv2(x))))

        x = x.view(-1, 32 * 16 * 16)

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))

        x_1, x_2, x_3, x_4 = torch.split(x, 5, dim=1)

        x_1 = self.qlayer1(x_1)
        x_2 = self.qlayer2(x_2)
        x_3 = self.qlayer3(x_3)
        x_4 = self.qlayer4(x_4)

        x = torch.cat([x_1, x_2, x_3, x_4], axis=1)

        x = self.fc3(x)
        return x


