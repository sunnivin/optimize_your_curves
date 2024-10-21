---
marp: true
theme: ngi-theme.css
paginate: true
footer: '![width:90 height:40](figures/logo/NGI/NGI_logo_transparent.gif)'
---




<!-- _class: title -->
<!-- _header: '_24.10.2024_' -->
# Optimize your curves, 
## (No gym required)

####
#### Oslo Python MeetUp
#### Sunniva Indrehus


--- 

<!-- paginate: true -->

```
$ whoami
```
---



# Agenda

## Curve Fitting 
  - What?
    - Example use cases  
  - Why? 
  - How? 
    - Attention: how to deal with bounds
 

---


# Start with a data set coming in, with a known model, how does it look like? 


---

# Give definitions: difference of function minimization and curve fitting 
---


> **Optimization**: an act, process, or methodology of making something (such as a design, system, or decision) as fully perfect, functional, or effective as possible 
specifically : the mathematical procedures (such as finding the maximum of a function) involved in this
<span style="display: block; text-align: right; font-style: italic; margin-top: 0.5rem;">*Merriam-Webster Dictionary*</span>



> **Curve Fitting**: The process of defining a function that describes the relationship between data points by discovering the parameters that best match the data with a curve.
<span style="display: block; text-align: right; font-style: italic; margin-top: 0.5rem;">*https://machinelearningmastery.com/curve-fitting-with-python/*</span>

---

# What is optimization? 
 - Find the extremas of a given function 
 - Find an optimal odel based on a given data set 
 - Find a set of optimal parameters on a given data set and model 

--- 

# What is Curve Fitting?

- Identifying the **best-fit curve** for a dataset with a known model 
  - Typically involves **minimizing** the difference between observed and predicted values
- Linear vs non-linear problem 
- Constrained vs unconstrained optimization
- **Real-life Examples**
  - Engineering, economics

---

# Key Concepts in Curve Fitting

- **Objective Function**: The function representing the error to minimize
- **Variables and Parameters**: Values modified to achieve the best fit
- **Constraints**: Optional limits on parameters
- Global vs local extremas
---

# **4. Common Curve Fitting Algorithms**

- **Gradient Descent**: Useful for optimizing parameters in large datasets
- **Simplex Method**: Applicable in linear problems
- **Levenberg-Marquardt**: For non-linear least squares fitting

---

# Curve fitting vs. model optimization 


| Aspect              | Curve Fitting                                   | Model Optimization                              |
|:---------------------|:------------------------------------------------|:------------------------------------------------|
| **Scope**           | Specific; find a curve that fits data | Broad; enhance model performance in various contexts |
| **Applications**     | Scientific, engineering, and data analysis | Machine learning, operations research, statistics, etc. |
| **Techniques**      | Primarily uses least squares regression, polynomial fitting, non-linear fitting | Includes hyperparameter tuning, model selection, regularization, etc. |
| **Goal**            | Model relationships between variables through a curve | Improve performance across various model types |
| **Context**         | Specific to approximating data with mathematical functions | General performance optimization for predictive models |


---


# Introduction to `lmfit`


- A Python library designed for **curve fitting** and parameter optimization
- Built on SciPy’s optimization capabilities
- Manages uncertainties and parameter correlations
- Supports constraints for fitting


---

<!-- _class: split-text -->


# Handeling bounds 

<div class=ldiv>

#

## [scipy.optimize.least_squares](https://docs.scipy.org/doc/scipy/reference/optimize.html#least-squares-and-curve-fitting)

- `bounds`2-tuple of array_like or Bounds, optional 

</div>


<div class=rdiv>

#

## [lmfit](https://lmfit.github.io/lmfit-py/bounds.html)

- Bounds set through the `Param` class

</div>


---


# **6. Demo: Curve Fitting with `lmfit`**

### Step 1: Problem Setup

```python
import numpy as np
import matplotlib.pyplot as plt
from lmfit import Model

def model_function(x, a, b, c):
    return a * np.exp(-b * x) + c

x_data = np.linspace(0, 10, 100)
y_true = model_function(x_data, a=3, b=1, c=0.5)
noise = np.random.normal(0, 0.2, x_data.shape)
y_data = y_true + noise

plt.scatter(x_data, y_data, label='Noisy Data')
plt.plot(x_data, y_true, color='red', label='True Model')
plt.legend()
plt.show()
```

---



# **3. Optimization: Key Concepts**

- **Objective Function**: The function to minimize or maximize
- **Variables and Parameters**: Values adjusted to optimize the function
- **Constraints**: Optional limits on variables
- **Global vs Local Minima/Maxima**: 
  - Global: The overall best solution
  - Local: A suboptimal solution

---

# **4. Common Optimization Algorithms**

- **Gradient Descent**: Used in large-scale problems like machine learning
- **Simplex Method**: Useful for linear programming
- **Levenberg-Marquardt**: For non-linear least squares problems

---

---

# **7. Interpreting the Results**

- **Parameter Estimates**: Best-fit values for `a`, `b`, and `c`
- **Fit Report**: Provides uncertainties and goodness-of-fit statistics
- **Visualization**: Compare the fitted model to the noisy data

---

# **8. Extending the Example**

- **Adding Constraints**:
  - Constrain parameters (e.g., `a > 0`)
- **Fitting Different Models**:
  - Experiment with other functions (e.g., polynomials, sine)
- **Advanced Features**:
  - Handle multiple datasets, parameter bounds, and more

---
<!--
class: center, middle
-->

# <div style="text-align: center;">:sparkles: :woman_technologist: Let's see some code :woman_technologist: :sparkles: </div>

