import numpy as np
import lmfit
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend


# Define Rosenbrock's Banana Function
def rosenbrock(x, y, a=1, b=100):
    return (a - x) ** 2 + b * (y - x**2) ** 2


# Generate synthetic data points
def generate_data(num_points=100, noise_level=0.1):
    x_true = np.linspace(-2, 2, num_points)
    y_true = x_true**2  # We expect y = x^2 for Rosenbrock
    noise = np.random.normal(0, noise_level, size=y_true.shape)  # Add noise
    y_observed = y_true + noise
    return x_true, y_observed


# Create a dataset
x_data, y_data = generate_data(num_points=100, noise_level=1.0)


# Define the objective function
def objective(params):
    # Get the parameters
    a = params["a"]
    b = params["b"]

    # Model predictions
    y_pred = a - x_data**2  # Compute y values based on Rosenbrock's function model
    return y_data - y_pred  # Return residuals


# Initial guess for the parameters
initial_params = lmfit.Parameters()
initial_params.add("a", value=1.0)  # Initial guess for parameter a
initial_params.add("b", value=100.0)  # Initial guess for parameter b

# Perform the optimization
result = lmfit.minimize(objective, initial_params)

# Print the results
print(result.message)
print(
    f"Optimized parameters: a = {result.params['a'].value}, b = {result.params['b'].value}"
)
print(
    f"Minimum value of Rosenbrock's function (sum of squares of residuals): {result.chisqr}"
)

# Optional: Plot the data and the fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, label="Observed Data", color="red", alpha=0.6)
plt.plot(
    x_data,
    rosenbrock(
        result.params["a"].value,
        x_data**2,
        a=result.params["a"].value,
        b=result.params["b"].value,
    ),
    label="Fitted Curve",
    color="blue",
)
plt.title("Rosenbrock's Banana Function Optimization")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.savefig("rosenbrock.png")
