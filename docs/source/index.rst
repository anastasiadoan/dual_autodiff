.. dual_autodiff documentation master file, created by
   sphinx-quickstart on Wed Dec 11 17:40:42 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

dual_autodiff documentation
===========================

Hello! Welcome to dual_autodiff user guide! I hope you enjoy the package and thanks for using it!
This package implements forward-mode automatic differentiation using dual numbers, a powerful technique of modern deep learning systems. Just as complex numbers consist of real and imaginary parts, dual numbers comprise real and dual components. However, while complex numbers use the imaginary unit *i* where *i²* = -1, dual numbers employ a dual unit *ε* where *ε²* = 0.

Forward-mode automatic differentiation is particularly efficient for functions with few input variables but many outputs - a common scenario in neural networks with small input layers and larger output layers. The method computes exact derivatives without relying on numerical approximations, making it both precise and computationally efficient.

The dual number system provides an mathematical framework for automatic differentiation. A dual number takes the form *a + bε*, where '*a*' represents the real component and '*b*' represents the dual component. This structure, combined with the fundamental property *ε²* = 0, enables direct computation of derivatives through algebraic manipulation rather than numerical limits or symbolic differentiation.

This implementation provides a robust foundation for gradient-based optimization tasks, particularly in machine learning applications where accurate and efficient derivative computation is essential. 

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   tutorials
   api_reference
