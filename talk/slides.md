---
marp: true
theme: ngi-theme.css
paginate: true
footer: '![width:90 height:40](figures/logo/NGI/NGI_logo_transparent.gif)'
---




<!-- _class: title -->
<!-- _header: '_24.10.2024_' -->
<!-- paginate: false -->
# Optimize your curves, 
## (No gym required)

####
#### Oslo Python MeetUp
#### Sunniva Indrehus


--- 

<!-- _class: title -->
<!-- paginate: false -->
# :chart_with_upwards_trend: + :muscle: + :snake: = :question: 

--- 

<!-- paginate: true -->

```
echo $(whoami)
```
---



# Agenda

- Problem 
- Curve fitting 
- `lmfit`
- Demo 

--- 
# Problem

|![](figures/plot/observed_low.png)|
|:--:|
| Which model parameters describe this data? |




<!-- - What are the optimal model parameters for my data?  -->

---


> **Optimization**: an act, process, or methodology of making something (such as a design, system, or decision) as fully perfect, functional, or effective as possible 
specifically : the mathematical procedures (such as finding the maximum of a function) involved in this


> **Curve Fitting**: the empirical determination of a curve or function that approximates a set of data
<span style="display: block; text-align: right; font-style: italic; margin-top: 0.5rem;">*Merriam-Webster Dictionary*</span>

---

# What *is* Curve Fitting?

* Identify the **best-fit curve** for a dataset with a known model 
    * **Minimize** the difference between *observed* and *predicted* values
        $$ 
        \chi^2 = \sum_{i=1}^{N} \frac{(y_i^\text{obs} - y_i^\text{pred})^2}{\sigma_i^2} 
        $$
* Categories of problems  
    * Linear vs non-linear 
      $$ 
      y_1 = ax + b \qquad \text{vs} \quad y_2 = \sin(\omega t)\text{e}^{-x^2}
      $$
    * Unconstrained vs Constrained
      $$
        a\in [-\infty,\infty] \quad \text{vs} \quad a \in [-\pi,\pi/3]
      $$



---

# Difference between *observed* and *predicted* values 



<div class="twocols">


##

![](figures/plot/observed_vs_predicted_low.png)



<p class="break"></p>

###
![](figures/plot/chi_square_plot_low.png)

</div>




---

# The real world is complicated

| |
|-----|
|![](figures/plot/true_model_sine.png)|
 
--- 

# Real (NGI work) life example 

<div class="twocols">


##
![w:450 h:350](figures/illustrations/full_model.png)
Offshore structure



<p class="break"></p>

###
![w:450 h:350](figures/illustrations/scaled_pile_head_equal_beginning.png)
Horizontal displacement curves under load

</div>


--- 


<!-- paginate: true -->

# Curve fitting requirements 
  - Provide estimates of parameter uncertanties
  - Handle non-linear problem formulations
  - Easy changebility of the optimization algorithm 
  - High level functionality for handling parameter [bounds](https://lmfit.github.io/lmfit-py/bounds.html)
  


--- 

# Recommended tool (by me) 


| **Topic**                        | **Details**                                                                         |
|:----------------------------------|:-------------------------------------------------------------------------------------|
| Library Name                 | `lmfit`                                                                             |
| GitHub Stars                 | :star: 1.1k                                                                              |
| Last Commit Date           | 13.10.2024 (on 22.10.2024)                                             |
| Description                  | High-level interface to non-linear optimization and curve fitting problems          |
| Built On                     | SciPy’s [`curve_fit`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) |

---



# <div style="text-align: center;">:sparkles: Let's see some code :sparkles: </div>

---


# Problem set up
```python
from lmfit import Minimizer, create_params

def residual(parameters, x, data):
    model = (
        parameters["amp"]
        * np.sin(x * parameters["omega"] + parameters["shift"])
        * np.exp(-x * x * parameters["decay"])
    )
    return model - data

parameters_initial = create_params(
    amp=10,
    decay=0.1,
    omega=3.0,
    shift=value=0.0,
)

minimizer = Minimizer(residual, parameters_initial, fcn_args=(x, data))
result = minimizer.minimize(method="least_squares")
```

--- 

# Handeling bounds 

```python
from lmfit import Parameters 

params = Parameters()
params.add('amp', value=10, min=0)
params.add('decay', value=0.1)
params.add('shift', value=0.0, min=-np.pi/2., max=np.pi/2.)
params.add('omega', value=3.0)

```

```python
from lmfit import create_params

params = create_params(amp=dict(value=10, min=0),
                       decay=0.1,
                       omega=3,
                       shift=dict(value=0, min=-np.pi/2, max=np.pi/2))
```


---


# Interperet simulation results

```bash
[[Fit Statistics]]
    # fitting method   = least_squares
    # function evals   = 58
    # data points      = 301
    # variables        = 4
    chi-square         = 12.1867036
    reduced chi-square = 0.04103267
    Akaike info crit   = -957.236198
    Bayesian info crit = -942.407756
[[Variables]]
    amp:    5.03088066 +/- 0.04005821 (0.80%) (init = 10)
    decay:  0.02495457 +/- 4.5396e-04 (1.82%) (init = 0.1)
    omega:  2.00026311 +/- 0.00326183 (0.16%) (init = 3)
    shift: -0.10264955 +/- 0.01022294 (9.96%) (init = 0)
[[Correlations]] (unreported correlations are < 0.100)
    C(omega, shift) = -0.7852
    C(amp, decay)   = +0.5840
    C(amp, shift)   = -0.1179
```
---


# <div style="text-align: center;">:woman_technologist: Demo :woman_technologist:  </div>

---

<!-- _class: title -->
# :chart_with_upwards_trend: + :muscle: + :snake: = :question: 

--- 

<!-- _class: title -->
# :chart_with_upwards_trend: + :muscle: + :snake: = :heart: 
