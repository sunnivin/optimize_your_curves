import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend

# Create data to be fitted
x = np.linspace(0, 15, 301)
np.random.seed(2021)
amp = 5.0
omega = 2.0
shift = -0.1
decay = 0.025
data = amp * np.sin(omega * x + shift) * np.exp(-x * x * decay) + np.random.normal(
    size=x.size, scale=0.2
)


# Define the model function
def model_func(x, amp, omega, shift, decay):
    return amp * np.sin(omega * x + shift) * np.exp(-x * x * decay)


# Initial guess for the parameters
initial_guess = [10, 3.0, 0.0, 0.1]

# Perform the curve fitting
popt, pcov = curve_fit(model_func, x, data, p0=initial_guess)

# Calculate the fitted data
fitted_data = model_func(x, *popt)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, data, "+", label="Data", color="red")
plt.plot(x, fitted_data, label="Fitted Curve", color="blue")
plt.axhline(
    0, color="gray", lw=0.5, ls="--"
)  # Add a horizontal line at y=0 for reference
plt.title("Curve Fitting with scipy.optimize.curve_fit")
plt.xlabel("x")
plt.ylabel("Data and Fitted Curve")
plt.legend()
plt.grid()
plt.savefig("parameters_values_scipy.png")
