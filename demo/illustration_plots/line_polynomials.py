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

# Fit a third-order polynomial
fit_params_3 = np.polyfit(x, y_observed, 3)
y_predicted_3 = np.polyval(fit_params_3, x)

# Fit a fifth-order polynomial
fit_params_5 = np.polyfit(x, y_observed, 5)
y_predicted_5 = np.polyval(fit_params_5, x)

# Calculate residuals for linear fit
residuals = y_observed - y_predicted

# Calculate chi-square values
chi_square = (residuals**2) / np.var(y_observed)

# Type variable
plot_type: str = "low"

# Data plot
plt.scatter(x, y_observed, color="red", label="Data", alpha=0.6)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(f"data_{plot_type}.png", bbox_inches="tight", pad_inches=0.03)
plt.close()


# One and one illustration
# Data plot with linear, third, and fifth-order fits
plt.scatter(x, y_observed, color="red", label="Data", alpha=0.6)
plt.plot(x, y_predicted, color="blue", label="Linear Fit", zorder=2)
plt.text(
    0.5,
    0.95,
    f"$y_{{linear}} = {fit_params[0]:.2f}x + {fit_params[1]:.2f}$",
    color="blue",
    fontsize=10,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(f"data_model_first_{plot_type}.png", bbox_inches="tight", pad_inches=0.03)
plt.close()

# Data plot with linear, third, and fifth-order fits
plt.scatter(x, y_observed, color="red", label="Data", alpha=0.6)
plt.plot(x, y_predicted_3, color="green", label="3rd Order Fit", zorder=3)
plt.text(
    0.5,
    0.90,
    f"$y_{{3rd}} = {fit_params_3[0]:.2f}x^3 + {fit_params_3[1]:.2f}x^2 + {fit_params_3[2]:.2f}x + {fit_params_3[3]:.2f}$",
    color="green",
    fontsize=10,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(f"data_model_third_{plot_type}.png", bbox_inches="tight", pad_inches=0.03)
plt.close()


# Data plot with linear, third, and fifth-order fits
plt.scatter(x, y_observed, color="red", label="Data", alpha=0.6)
plt.plot(x, y_predicted_5, color="purple", label="5th Order Fit", zorder=4)
plt.text(
    0.5,
    0.85,
    f"$y_{{5th}} = {fit_params_5[0]:.2f}x^5 + {fit_params_5[1]:.2f}x^4 + {fit_params_5[2]:.2f}x^3 + {fit_params_5[3]:.2f}x^2 + {fit_params_5[4]:.2f}x + {fit_params_5[5]:.2f}$",
    color="purple",
    fontsize=10,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(f"data_model_fifth_{plot_type}.png", bbox_inches="tight", pad_inches=0.03)
plt.close()


# Data plot with linear, third, and fifth-order fits
plt.scatter(x, y_observed, color="red", label="Data", alpha=0.6)
plt.plot(x, y_predicted, color="blue", label="Linear Fit", zorder=2)
plt.plot(x, y_predicted_3, color="green", label="3rd Order Fit", zorder=3)
plt.plot(x, y_predicted_5, color="purple", label="5th Order Fit", zorder=4)

# Add fit equations to the plot
plt.text(
    0.5,
    0.95,
    f"$y_{{linear}} = {fit_params[0]:.2f}x + {fit_params[1]:.2f}$",
    color="blue",
    fontsize=10,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.text(
    0.5,
    0.90,
    f"$y_{{3rd}} = {fit_params_3[0]:.2f}x^3 + {fit_params_3[1]:.2f}x^2 + {fit_params_3[2]:.2f}x + {fit_params_3[3]:.2f}$",
    color="green",
    fontsize=10,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.text(
    0.5,
    0.85,
    f"$y_{{5th}} = {fit_params_5[0]:.2f}x^5 + {fit_params_5[1]:.2f}x^4 + {fit_params_5[2]:.2f}x^3 + {fit_params_5[3]:.2f}x^2 + {fit_params_5[4]:.2f}x + {fit_params_5[5]:.2f}$",
    color="purple",
    fontsize=10,
    ha="center",
    transform=plt.gca().transAxes,
)

# Customize the plot
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(f"data_model_{plot_type}.png", bbox_inches="tight", pad_inches=0.03)
plt.close()

# Plot 1: Observed vs Predicted for all fits
plt.scatter(x, y_observed, color="red", label="Data", alpha=0.6)
plt.plot(x, y_predicted, color="blue", label="Linear Fit", zorder=2)
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
    0.90,
    "$y_{fit}" + f"= {fit_params[0]:.2f}x + {fit_params[1]:.2f}$",
    color="blue",
    fontsize=12,
    ha="center",
    transform=plt.gca().transAxes,
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig(
    f"observed_vs_predicted_{plot_type}.png", bbox_inches="tight", pad_inches=0.03
)
plt.close()

# Plot 2: Residuals for Linear Fit
plt.bar(x, residuals, color="purple", alpha=0.6)
plt.axhline(0, color="black", linewidth=1)
plt.xlabel("x")
plt.ylabel("Residuals (Observed - Predicted)")
plt.savefig(f"residuals_plot_{plot_type}.png", dpi=300)
plt.close()

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
plt.savefig(f"chi_square_plot_{plot_type}.png", bbox_inches="tight", pad_inches=0.03)
plt.close()
