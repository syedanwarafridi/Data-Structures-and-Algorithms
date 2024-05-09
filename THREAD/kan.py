import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from scipy.interpolate import BSpline
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import numpy as np
from scipy.interpolate import BSpline

# Custom Activation Function with Spline
class LearnableSplineActivation(nn.Module):
    def __init__(self, order, num_knots):
        super().__init__()
        self.order = order
        self.num_knots = num_knots
        # The number of coefficients for B-spline should be `num_knots + order`
        self.coefficients = nn.Parameter(torch.randn(num_knots + order, dtype=torch.float32))

    def forward(self, x):
        # Create the B-spline with proper knots
        # For an order-k B-spline, you need `num_knots + 2 * order` knots (including the order-related repetitions)
        knots = np.linspace(0, 1, self.num_knots + 2 * self.order)

        # Ensure the number of coefficients matches the expected count for this order
        spline = BSpline(knots, self.coefficients.detach().numpy(), self.order)

        # Apply the spline to the input
        spline_results = [spline(val.item()) for val in x.view(-1)]

        # Convert the results to a tensor
        spline_tensor = torch.tensor(spline_results, dtype=x.dtype, device=x.device)

        # Return with the same shape as the input
        return spline_tensor.view_as(x)




# KAN (Learnable Activation Network)
class KAN(nn.Module):
    def __init__(self, input_size, hidden_sizes, output_size, spline_order, num_knots):
        super().__init__()
        # Create layers with learnable spline activation functions
        layers = []
        prev_size = input_size
        for hidden_size in hidden_sizes:
            layers.append(nn.Linear(prev_size, hidden_size))
            layers.append(LearnableSplineActivation(spline_order, num_knots))
            prev_size = hidden_size
        layers.append(nn.Linear(prev_size, output_size))
        self.network = nn.Sequential(*layers)

    def forward(self, x):
        return self.network(x)

# Sample Usage for Regression Task
x = torch.linspace(-1, 1, 100)
y = torch.sin(2 * np.pi * x) + 0.1 * torch.randn_like(x)  # Add some noise for realism

# Define the model with appropriate parameters
model = KAN(1, [32, 32], 1, 3, 4)  # (input_size, hidden_sizes, output_size, spline_order, num_knots)

# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
num_epochs = 1000
for epoch in range(num_epochs):
    optimizer.zero_grad()
    y_pred = model(x.view(-1, 1))
    loss = criterion(y_pred, y.view(-1, 1))
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: Loss = {loss.item()}")

# Plot the results
plt.scatter(x, y, label="Data")
plt.plot(x, y_pred.detach(), label="KAN Prediction", color='red')
plt.legend()
plt.title("KAN Regression")
plt.show()
