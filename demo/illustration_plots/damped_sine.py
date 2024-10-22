import numpy as np
from lmfit import Minimizer, create_params, report_fit
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")

# create data to be fitted
x = np.linspace(0, 15, 301)
np.random.seed(2021)
amp = 5.0
omega = 2.0
shift = -0.1
decay = 0.025
data = amp * np.sin(omega * x + shift) * np.exp(-x * x * decay) + np.random.normal(
    size=x.size, scale=0.2
)


def residual(parameters, x, data):
    model = (
        parameters["amp"]
        * np.sin(x * parameters["omega"] + parameters["shift"])
        * np.exp(-x * x * parameters["decay"])
    )
    return model - data


parameters_initial = create_params(
    amp=dict(value=10, min=0),
    decay=0.1,
    omega=3.0,
    shift=dict(value=0.2, min=-np.pi / 2.0, max=np.pi / 2),
)

initial_model = (
    parameters_initial["amp"].value
    * np.sin(x * parameters_initial["omega"].value + parameters_initial["shift"].value)
    * np.exp(-x * x * parameters_initial["decay"].value)
)

minimizer = Minimizer(residual, parameters_initial, fcn_args=(x, data))
result = minimizer.minimize(method="least_squares")

# calculate final
final = data + result.residual

# write error report
report_fit(result)

# Plot original data, initial model, and final fitted model
plt.scatter(x, data, label="data", color="red", alpha=0.6)
plt.plot(x, initial_model, label="initial", linestyle="--", color="green")
plt.plot(x, final, label="final", color="blue")
plt.legend()
plt.savefig("parameters_values_lmfit.png", bbox_inches="tight", pad_inches=0.03)

# Additional plot: true model
true_model = amp * np.sin(omega * x + shift) * np.exp(-x * x * decay)

# Plotting the data and the true model
plt.figure()
plt.scatter(x, data, label="Data", color="red", alpha=0.6)
plt.plot(x, true_model, "--", label="True", color="green", linewidth=2)

# Adding the true model expression as text
model_text = r"$y = %.f \sin(%.f x  %.2f) \, e^{-x^2 \cdot %.3f}$" % (
    amp,
    omega,
    shift,
    decay,
)
plt.text(0.5, 0.8, model_text, fontsize=12, transform=plt.gca().transAxes)

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig("true_model_sine.png", bbox_inches="tight", pad_inches=0.03)
