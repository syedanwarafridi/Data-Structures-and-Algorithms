import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt


# Custom learnable activation layer with spline parameters
class LearnableActivation(layers.Layer):
    def __init__(self, output_dim, grid_size=5, base_activation=None, **kwargs):
        super().__init__(**kwargs)
        self.output_dim = output_dim
        self.grid_size = grid_size
        self.base_activation = base_activation
        # Initialize learnable spline parameters
        self.spline_params = self.add_weight(
            shape=(grid_size, output_dim),  # Updated to match output_dim
            initializer="random_normal",
            trainable=True
        )

    def call(self, inputs):
        # Apply base activation if provided
        base_out = self.base_activation(inputs) if self.base_activation else inputs
        # Apply spline parameters
        spline_out = tf.matmul(inputs, self.spline_params)  # This gives correct output shape
        return base_out + spline_out


# Build a simple LAN model with learnable activation functions
def build_lan(input_dim, width, depth, grid_size):
    inputs = keras.Input(shape=(input_dim,))
    x = inputs
    for _ in range(depth):
        # Fully connected layer
        x = layers.Dense(width)(x)
        # Custom learnable activation with consistent dimensions
        x = LearnableActivation(width, grid_size, base_activation=tf.math.sin)(x)
    outputs = layers.Dense(1)(x)
    return keras.Model(inputs, outputs)


# Generate synthetic dataset for demonstration
def generate_synthetic_data(num_samples=1000):
    # Create x values between -2 and 2
    x = np.linspace(-2, 2, num_samples)
    # Define a synthetic function
    y = np.exp(np.sin(np.pi * x))
    return x, y


# Generate synthetic data
x, y = generate_synthetic_data()

# Create the LAN model
input_dim = 1
width = 128
depth = 5
grid_size = 5

model = build_lan(input_dim, width, depth, grid_size)
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(x, y, epochs=10, batch_size=32, verbose=1)

# Make predictions
y_pred = model.predict(x)

# Plot predictions against data
plt.scatter(x, y, s=2, c='b', label='Data')
plt.plot(x, y_pred, 'r', label='Prediction')
plt.xlabel('x')
plt.ylabel('y')
plt.title('LAN Predictions vs. Synthetic Data')
plt.legend()
plt.show()
