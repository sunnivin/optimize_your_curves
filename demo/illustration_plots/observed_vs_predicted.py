import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend

# Create some example data
np.random.seed(42)
x = np.linspace(0, 10, 20)
true_params = [2.5, -1.2]  # true slope and intercept for a linear model
y_true = true_params[0] * x + true_params[1]
y_observed = y_true + np.random.normal(scale=1.0, size=len(x))  # add some noise

# Fit a simple linear model to get the predicted values
fit_params = np.polyfit(x, y_observed, 1)
y_predicted = np.polyval(fit_params, x)

# Plot the observed and predicted data
plt.figure(figsize=(10, 6))
plt.scatter(x, y_observed, color="red", label="Observed Data", zorder=3)
plt.plot(x, y_predicted, color="blue", label="Predicted (Fitted) Curve", zorder=2)
plt.plot(
    x, y_true, color="green", linestyle="--", label="True Underlying Function", zorder=1
)

# Add lines to show residuals
for i in range(len(x)):
    plt.plot(
        [x[i], x[i]],
        [y_observed[i], y_predicted[i]],
        color="gray",
        linestyle=":",
        zorder=0,
    )

# Customize the plot
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Illustration of Observed vs Predicted Values")
plt.legend()
plt.grid(alpha=0.3)

# Save the figure
plt.savefig("observed_vs_predicted.png", dpi=300)
