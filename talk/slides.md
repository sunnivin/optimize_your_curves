---
marp: true
theme: ngi-theme.css
paginate: true
footer: '![width:90 height:40](figures/logo/NGI/NGI_logo_transparent.gif)'
---




<!-- _class: title -->
<!-- _header: '_24.10.2024_' -->
# Optimize me

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
  - What is it? 
  - Why is it important? 
  - Example use cases 
  - How does it work? 
- Key considerations 
  - Global vs Local Minima/Maxima 

---

> **Curve Fitting**: The process of defining a function that describes the relationship between data points by discovering the parameters that best match the data with a curve.
<span style="display: block; text-align: right; font-style: italic; margin-top: 0.5rem;">*https://machinelearningmastery.com/curve-fitting-with-python/*</span>

---

# What is Curve Fitting?

- Identifying the **best-fit curve** for a dataset with a known model 
  - Typically involves **minimizing** the difference between observed and predicted values
- Linear vs non-linear problem 
- Constrained vs unconstrained optimization
- **Real-life Examples**
  - Engineering, economics

---


---

<!-- _class: split-text -->



# Our [(PEP)](https://peps.python.org/pep-0000/) best friends

<div class=ldiv>


#

#### [PEP 484](https://peps.python.org/pep-0484/)


- Type annotation
  - Released 2015-09-13
- Tool(s)
  - [mypy](https://mypy.readthedocs.io/en/stable/)

</div>


<div class=rdiv>

#

#### [PEP 8](https://peps.python.org/pep-0008/)

- Style guide for Python Code
  - Released 2013-08-01
- Tool(s)
  - [black](https://black.readthedocs.io/en/stable/) or [ruff](https://docs.astral.sh/ruff/)
  - [flake8](https://flake8.pycqa.org/en/latest/)
  - [isort](https://pycqa.github.io/isort/)

</div>



# Key Concepts in Curve Fitting

- **Objective Function**: The function representing the error to minimize
- **Variables and Parameters**: Values modified to achieve the best fit
- **Constraints**: Optional limits on parameters
- **Global vs Local extremas
---

# **4. Common Curve Fitting Algorithms**

- **Gradient Descent**: Useful for optimizing parameters in large datasets
- **Simplex Method**: Applicable in linear problems
- **Levenberg-Marquardt**: For non-linear least squares fitting

---

# **5. Introduction to `lmfit`**

- **What is `lmfit`?**
  - A Python library designed for **curve fitting** and parameter optimization
  - Built on SciPy’s optimization capabilities
- **Advantages**:
  - Manages uncertainties and parameter correlations
  - Supports constraints for fitting
  - Employs advanced algorithms for improved convergence

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

# Agenda

## Optimization 
  - What?
  - Why? 
  - Example use cases 
  - How ? 
- Attention points 
  - Global vs Local Minima/Maxima**: 
  
---

> **Optimization**: an act, process, or methodology of making something (such as a design, system, or decision) as fully perfect, functional, or effective as possible 
specifically : the mathematical procedures (such as finding the maximum of a function) involved in this
<span style="display: block; text-align: right; font-style: italic; margin-top: 0.5rem;">*Merriam-Webster Dictionary*</span>


--- 






--- 

> curve fitting is appropriate when you want to define the function explicitly, then discover the parameters of your function that best fit a line to the data.
<span style="display: block; text-align: right; font-style: italic; margin-top: 0.5rem;">*https://machinelearningmastery.com/curve-fitting-with-python/*</span>


--- 

# What is Optimization?

- Finding the **best solution** to a problem
  - Typically **minimizing** or **maximizing** an objective function
- Common applications:
  - Minimizing cost
  - Maximizing efficiency
  - Curve fitting in data science

---

# **2. Types of Optimization Problems**

- **Linear vs Non-linear Optimization**
  - Linear: Straight-line relationships
  - Non-linear: Curved relationships
- **Constrained vs Unconstrained Optimization**
  - Constraints restrict the search space
- **Real-life Examples**
  - Engineering, economics, machine learning

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

# **5. Introduction to `lmfit`**

- **What is `lmfit`?**
  - A Python library for **curve fitting** and **optimization**
  - Built on top of SciPy's optimization routines
- **Advantages**:
  - Handles uncertainties and correlations between parameters
  - Supports constraints
  - Uses advanced algorithms for better convergence

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

### Step2: problem setup

```python
model = Model(model_function)
params = model.make_params(a=2, b=0.5, c=1)

result = model.fit(y_data, params, x=x_data)

print(result.fit_report())
plt.scatter(x_data, y_data, label='Noisy Data')
plt.plot(x_data, result.best_fit, label='Fitted Model', color='green')
plt.legend()
plt.show()
```
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

# **9. Optimization vs Machine Learning**

| **Aspect**            | **Optimization**                     | **Machine Learning**                |
|:-----------------------|:--------------------------------------|:-------------------------------------|
| **Purpose**           | Solving a specific mathematical problem | Learning from data                 |
| **Scope**             | Static problems                      | Dynamic, data-driven problems       |
| **Use of Data**       | May not require data                 | Always requires data                |
| **Objective**         | Exact solution (minimize/maximize)   | Generalize to new data              |
| **Role of Optimization** | Primary focus                    | A tool for minimizing loss          |

---

# **10. Conclusion and Takeaways**

- **Optimization**: Finding the best parameters for a given objective
- **`lmfit`**: Python library that simplifies non-linear optimization
- **Machine Learning**: Uses optimization but focuses on learning from data

**Thank you! 🙌**
