import numpy as np

from lmfit import Minimizer, create_params, report_fit

import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("Agg")


method = "least_squares"
method = "leastsq"
# method = "tnc"
# method = "cg"

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
result = minimizer.minimize(method=method)

# calculate final
final = data + result.residual

report_fit(result)


plt.scatter(x, data, label="data", color="red", alpha=0.6)
plt.plot(x, initial_model, label="initial", linestyle="--", color="green")
plt.plot(x, final, label="final", color="blue")
plt.legend()
plt.savefig(f"parameters_values_{method}.png", bbox_inches="tight", pad_inches=0.03)
