import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")  # Use a non-interactive backend

# Create some example data
np.random.seed(42)
x = np.linspace(0, 10, 20)
true_params = [2.5, 1.2]  # true slope and intercept for a linear model
y_true = true_params[0] * x + true_params[1]
y_observed = y_true + np.random.normal(scale=1.0, size=len(x))  # add some noise

# Fit a simple linear model to get the predicted values
fit_params = np.polyfit(x, y_observed, 1)
y_predicted = np.polyval(fit_params, x)

# Calculate residuals
residuals = y_observed - y_predicted

# Calculate chi-square values
chi_square = (residuals**2) / np.var(y_observed)

# Type variable
plot_type: str = "low"


# Data plot
# plt.figure(figsize=(10, 5))
plt.scatter(x, y_observed, color="red", label="Data", zorder=3)

# Add function expressions
plt.text(
    0.5,
    0.95,
    "$y_{model}" + f"= {true_params[0]}x + {true_params[1]}$",
    color="green",
    fontsize=12,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)

# Save the figure
plt.savefig(f"observed_{plot_type}.png", dpi=300)
plt.close()  # Close the figure to free memory


# Plot 1: Observed vs Predicted
plt.figure(figsize=(10, 5))
plt.scatter(x, y_observed, color="red", label="Data", zorder=3)
plt.plot(x, y_true, color="green", linestyle="--", label="Model", zorder=1)
plt.plot(x, y_predicted, color="blue", label="Fit", zorder=2)


# Add lines to show residuals
for i in range(len(x)):
    plt.plot(
        [x[i], x[i]],
        [y_observed[i], y_predicted[i]],
        color="gray",
        linestyle=":",
        zorder=0,
    )
plt.text(
    0.5,
    0.95,
    "$y_{model}" + f"= {true_params[0]}x + {true_params[1]}$",
    color="green",
    fontsize=12,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.text(
    0.5,
    0.90,
    "$y_{fit}" + f"= {fit_params[0]:.2f}x + {fit_params[1]:.2f}$",
    color="blue",
    fontsize=12,
    ha="center",
    transform=plt.gca().transAxes,
)

# Customize the plot
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)

# Save the figure
plt.savefig(f"observed_vs_predicted_{plot_type}.png", dpi=300)
plt.close()  # Close the figure to free memory

# Plot 2: Residuals
plt.figure(figsize=(10, 5))
plt.bar(x, residuals, color="purple", alpha=0.6)
plt.axhline(0, color="black", linewidth=1)
plt.xlabel("x")
plt.ylabel("Residuals (Observed - Predicted)")
plt.grid(alpha=0.3)

# Save the figure
plt.savefig(f"residuals_plot_{plot_type}.png", dpi=300)
plt.close()  # Close the figure to free memory

# Plot 3: Chi-Square values
plt.figure(figsize=(10, 5))
plt.bar(x, chi_square, color="orange", alpha=0.6)
plt.axhline(
    np.mean(chi_square),
    color="black",
    linewidth=1,
    linestyle="--",
    label=r"$\bar{\chi}^2$",
)
plt.xlabel("x")
plt.ylabel(r"$\chi^2$")
plt.legend()
plt.grid(alpha=0.3)

# Save the figure
plt.savefig(f"chi_square_plot_{plot_type}.png", dpi=300)
plt.close()  # Close the figure to free memory
