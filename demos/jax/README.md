# Introduction to JAX

[JAX](https://jax.readthedocs.io/en/latest/) is a framework for accelerated scientific computing that provides an alternative implementation of the NumPy API for linear algebra computation with added auto-differentiation and Just-in-Time (JIT) compilation. Unlike similar frameworks - e.g., PyTorch or TensorFlow - it works within a purely [functional programming](https://en.wikipedia.org/wiki/Functional_programming) paradigm.

The [Flax](https://flax.readthedocs.io/en/latest/index.html) and [Optax](https://optax.readthedocs.io/en/latest/index.html) packages extend JAX's capabilities to cover the easy definition and training of deep learning models.

## Demo Objectives

* How to manipulate tensors - i.e., JAX as an alternative to NumPy.
* How to use auto-differentiation and minimise arbitrary functions.
* How to build and train ML models from first principles - linear regression.
* How to build and train a deep learning model for image classification using Flax and Optax.

## Running the Demo

This demo spans several Jupyter notebook:

* `demos/jax/introduction_to_jax.ipynb`.
* `demos/jax/linear_regression.ipynb`.
* `demos/jax/mnist_with_flax_and_optax.ipynb`.

Make sure you have the necessary Python package requirements installed into a Jupyter kernel for it to run successfully.
