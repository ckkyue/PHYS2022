import numpy as np
import matplotlib.pyplot as plt

# Define the function for the transmission probability
def T(x):
    return 9 / (17 - 8*np.cos(x))

# Define the range of x values to plot
x = np.linspace(0, 4*np.pi, 10000)

# Evaluate the function for each x value
y = T(x)

# Create the plot
plt.plot(x, y, label="Quantum")
plt.xlabel(r"$\sqrt{mV_{1}/\hbar} \cdot L$")
plt.ylabel("Transmission probability")
plt.title("Transmission probability versus $\sqrt{mV_{1}/\hbar} \cdot L$")

# Add a horizontal line at y=1
plt.axhline(y=1, color='r', linestyle='--', label="Classical")

# Add a legend to the plot
plt.legend()

plt.savefig("A finite potential barrier T.png")
plt.show()
