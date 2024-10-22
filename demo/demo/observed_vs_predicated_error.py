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

# Calculate residuals
residuals = y_observed - y_predicted

# Create the main figure with two subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# First subplot: Observed vs Predicted
axs[0].scatter(x, y_observed, color="red", label="Observed Data", zorder=3)
axs[0].plot(x, y_predicted, color="blue", label="Predicted (Fitted) Curve", zorder=2)
axs[0].plot(
    x, y_true, color="green", linestyle="--", label="True Underlying Function", zorder=1
)

# Add lines to show residuals
for i in range(len(x)):
    axs[0].plot(
        [x[i], x[i]],
        [y_observed[i], y_predicted[i]],
        color="gray",
        linestyle=":",
        zorder=0,
    )

# Customize the first subplot
axs[0].set_xlabel("X values")
axs[0].set_ylabel("Y values")
axs[0].set_title("Observed vs Predicted Values")
axs[0].legend()
axs[0].grid(alpha=0.3)

# Second subplot: Residuals
axs[1].bar(x, residuals, color="purple", alpha=0.6)
axs[1].axhline(0, color="black", linewidth=1)
axs[1].set_xlabel("X values")
axs[1].set_ylabel("Residuals (Observed - Predicted)")
axs[1].set_title("Residuals Plot")
axs[1].grid(alpha=0.3)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig("observed_vs_predicted_with_residuals.png", dpi=300)
