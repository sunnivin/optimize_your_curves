import numpy as np

from lmfit import Minimizer, create_params, report_fit, minimize

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


# define objective function: returns the array to be minimized
def fcn2min(params, x, data):
    """Model a decaying sine wave and subtract data."""
    v = params.valuesdict()

    model = v["amp"] * np.sin(x * v["omega"] + v["shift"]) * np.exp(-x * x * v["decay"])
    return model - data


# create a set of Parameters
params = create_params(
    amp=dict(value=10, min=0),
    decay=0.1,
    omega=3.0,
    shift=dict(value=0.0, min=-np.pi / 2.0, max=np.pi / 2),
)

initial_model = (
    params["amp"].value
    * np.sin(x * params["omega"].value + params["shift"].value)
    * np.exp(-x * x * params["decay"].value)
)
# do fit, here with the default leastsq algorithm
minner = Minimizer(fcn2min, params, fcn_args=(x, data))
result = minner.minimize(method="least_squares")

# calculate final result
final = data + result.residual

# write error report
report_fit(result)

# try to plot results

plt.plot(x, data, "+", label="data", color="red")
plt.plot(x, initial_model, label="initial", linestyle="--", color="green")
plt.plot(x, final, label="final", color="blue")
plt.legend()
plt.savefig("parameters_values_lmfit.png")
