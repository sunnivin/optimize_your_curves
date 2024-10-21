---
marp: true
theme: ngi-theme.css
paginate: false
header: '_24.10.2024_'
footer: '![width:90 height:40](figures/logo/NGI/NGI_logo_transparent.gif)'



--- 
<!-- _class: title --> 
# Optimization


## 

#### 
#### Python MeetUp
#### Sunniva Indrehus

---
 
<!-- _class: title --> 
# Optimization

## 

![bg right w:600 h:450](figures/illustrations/new-core.png) 
#### 
#### Python MeetUp
#### Sunniva Indrehus


---

<!-- paginate: true -->

```
$ whoami
```
--- 

# Motivation and agenda 

- Why optimization? 
- How to do it with python
---


<!-- _footer: "![width:90 height:40](figures/logo/NGI/NGI_logo_transparent.gif)  *Figure credit: [Ali Bati](http://www.alibati.com/horse)* " -->

# What is optimization?

- Understand a simplified version of the real world 

![bg right w:400 h:350](figures/illustrations/horse.png) 

---

# Type of optimization problems  

- Linear vs. Non-linear 
- Constrained vs. Unconstrained 




--- 

# Real life example from Geotechical engineering


![bg right w:500 h:450](figures/illustrations/full_model.png)  

--- 

# Matchematical formulation of 

## Why?
 
:snake: Python is dynamically typed, and [PEP484 Type Hints](https://peps.python.org/pep-0484/) is not enforced during run time 

## What?

> Pydantic is the most widely used data validation library for Python.
> 
*[From the official docs](https://docs.pydantic.dev/latest/#why-use-pydantic)*

---

<!-- _footer: "![width:90 height:40](figures/logo/NGI/NGI_logo_transparent.gif)  *Figure credit: [Prashanth Rao](https://thedataquarry.com/posts/why-pydantic-v2-matters/)* " -->

# Pydantic v2

## A new core 

![bg right w:600 h:450](figures/illustrations/v1-v2.png)

- Validations outside of Python
- Recursive function calls with Rust and small overhead 

---

# Pydantic v2 

## (Some) new features
- Functionality for discriminated unions
- `pydantic.functional_validators` let you do validation without `base_model` (*e.g* a function)
    - Possibility to use `TypeAdapter` instead of `BaseModel`
- You can define `field_serializer` you can do *custom serialization* 

## Examples and inspiration 
- [Migration guide](https://docs.pydantic.dev/latest/migration/)
- [v1 to v2 video example](https://www.youtube.com/watch?v=sD_xpYl4fPU)

---

# Let's get our hands dirty 

--- 

# Data 
## [Wine reviews from Kaggle](https://www.kaggle.com/datasets/zynicide/wine-reviews)
 
```json
{'country': 'France',
 'description': 'Ripe in color and aromas, this chunky wine delivers heavy '
                'baked-berry and raisin aromas in front of a jammy, extracted '
                'palate. Raisin and cooked berry flavors finish plump, with '
                'earthy notes.',
 'id': 45100,
 'points': 85,
 'price': 10.0,
 'province': 'Maule Valley',
 'taster_name': 'Michael Schachner',
 'taster_twitter_handle': '@wineschach',
 'title': 'Balduzzi 2012 Reserva Merlot (Maule Valley)',
 'variety': 'Merlot',
 'vineyard': 'The Vineyard',
 'winery': 'Balduzzi'}
```
--- 

# Data model 

## Pydantic's job
- Ensure the `id` field always exists (this will be the primary key), and is an integer
- Ensure the `points` field is an integer
- Ensure the `price` field is a float
- Ensure the `country` field always has a non-null value – if it’s set as null or the country key doesn’t exist in the raw data, it must be set to Unknown. This is because the use case we defined will involve querying on country downstream
- Remove fields like designation, `province`, `region_1` and `region_2` if they have the value null in the raw data – these fields will not be queried on and we do not want to unnecessarily store null values downstream

--- 

# Demo

--- 
# Speed-up for *free*  :unlock:

| v1 | v2 
|:---| :---
| `root_validator` | `@model_validator/@field_validator`
| `wine = Wine(**sample_data)`| `wine = Wine(**sample_data)`| 
| `pprint(wine.dict(exclude_none=True, by_alias=True))`| `pprint(wine.model_dump(exclude_none=True, by_alias=True))`


---

# Speed-up with *investements* :moneybag:


| v2 | v2-optimized
| :--- | :---
| `class Wine(BaseModel)` | `class Wine(TypedDict)`
| `wine = Wine(**sample_data)`| `wines = WinesTypeAdapter.validate_python([sample_data])`



---

# Demo some benchmarking

All tests on Windows11, with WSL2:Ubuntu-22.04

## Example run times

129971 records $\cdot$ 5 = 649855 validation operations

| | v1 | v2 | v2-optimized
:-----|:------|:-----|:------
**All cases** | 45.380 | 6.944 | 3.582
**Average pr run** | 9.076 | 1.389 | 0.716
**Times speed up (v1)** | 1 | 6.534 | 12.678


--- 

# Sometimes tricky with linting 

## `mypy` integration

[Explanation](https://github.com/pydantic/pydantic/discussions/6517) of why `TypedDict` work with a `field_validator`, but violates PEP589 

See the different examples in `demo/v2/good_mypy.py` and `demo/v2/bad_mypy.py`

--- 
# Credit 

- [Pydantic v2 Plan](https://docs.pydantic.dev/latest/blog/pydantic-v2/) (accessed 22.08.2023)
- Terrence Dorsey and Samuel Colvin [Pydantic v2 Pre Release](https://docs.pydantic.dev/latest/blog/pydantic-v2-alpha/) (accessed 22.08.2023)
- Prashanth Rao, The Data Quarry, [Obtain a 5x speedup for free by upgrading to Pydantic v2](https://thedataquarry.com/posts/why-pydantic-v2-matters/) (accessed 22.08.2023)
- Yaakov Bressler in [Medium](https://blog.det.life/dont-write-another-line-of-code-until-you-see-these-pydantic-v2-breakthrough-features-5cdc65e6b448) (accessed 22.08.2023)
- Samuel Colvin at [PyCon US 2023](https://www.youtube.com/watch?v=pWZw7hYoRVU) (accessed 22.08.2023)
- Configuring [mypy with Pydantic](https://docs.pydantic.dev/latest/integrations/mypy/#configuring-the-plugin) (accessed 22.08.2023)
