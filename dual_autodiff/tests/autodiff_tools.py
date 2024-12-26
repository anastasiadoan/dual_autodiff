import pytest
import math
from dual_autodiff import Dual

# ---------------------------
# Initialization Tests
# ---------------------------
def test_initialization_with_non_numeric_real():
    with pytest.raises(TypeError):
        Dual("two", 1)

def test_initialization_with_non_numeric_dual():
    with pytest.raises(TypeError):
        Dual(2, "one")

def test_initialization_with_none():
    with pytest.raises(TypeError):
        Dual(None, 1)

def test_initialization_missing_arguments():
    with pytest.raises(TypeError):
        Dual(2)  # Missing dual part

# ---------------------------
# Arithmetic Operation Tests
# ---------------------------
def test_addition():
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x + y
    assert result == Dual(5, 3), "Dual addition failed."

    # Scalar addition
    result = x + 3
    assert result == Dual(5, 1), "Dual and scalar addition failed."

def test_subtraction():
    x = Dual(5, 3)
    y = Dual(3, 1)
    result = x - y
    assert result == Dual(2, 2), "Dual subtraction failed."

    # Scalar subtraction
    result = x - 2
    assert result == Dual(3, 3), "Dual and scalar subtraction failed."

    # Reverse subtraction
    result = 10 - x
    assert result == Dual(5, -3), "Reverse scalar and dual subtraction failed."

def test_multiplication():
    x = Dual(2, 1)
    y = Dual(3, 2)
    result = x * y
    expected = Dual(6, 7)  # 2*3 + (2*2 + 1*3)ε = 6 + 7ε
    assert result == expected, "Dual multiplication failed."

    # Scalar multiplication
    result = x * 3
    assert result == Dual(6, 3), "Dual and scalar multiplication failed."

def test_division():
    x = Dual(6, 2)
    y = Dual(3, 1)
    result = x / y
    expected = Dual(2.0, 0.0)  # 6/3 + (2*3 - 6*1)/3² = 2 + 0ε
    assert result == expected, "Dual division failed."

    # Scalar division
    result = x / 2
    assert result == Dual(3, 1), "Dual and scalar division failed."

    # Division by Dual with zero real part (raises error)
    with pytest.raises(ZeroDivisionError):
        x / Dual(0, 0)

    # Division by scalar zero (raises error)
    with pytest.raises(ZeroDivisionError):
        x / 0

def test_multiplication_with_incorrect_type():
    x = Dual(2, 1)
    with pytest.raises(TypeError):
        result = x * [1, 2, 3]

def test_addition_with_incorrect_type():
    x = Dual(2, 1)
    with pytest.raises(TypeError):
        result = x + "three"

def test_subtraction_with_incorrect_type():
    x = Dual(2, 1)
    with pytest.raises(TypeError):
        result = x - None

# ---------------------------
# Mathematical Function Tests
# ---------------------------
def test_sin():
    x = Dual(math.pi / 2, 1)
    result = x.sin()
    expected_real = math.sin(math.pi / 2)  # 1.0
    expected_dual = math.cos(math.pi / 2)  # 0.0
    assert math.isclose(result.real, expected_real, abs_tol=1e-9), "Dual sin real part incorrect."
    assert math.isclose(result.dual, expected_dual, abs_tol=1e-9), "Dual sin dual part incorrect."

def test_cos():
    x = Dual(0, 1)
    result = x.cos()
    expected_real = math.cos(0)  # 1.0
    expected_dual = -math.sin(0) * 1  # 0.0
    assert math.isclose(result.real, expected_real, abs_tol=1e-9), "Dual cos real part incorrect."
    assert math.isclose(result.dual, expected_dual, abs_tol=1e-9), "Dual cos dual part incorrect."

def test_tan():
    x = Dual(math.pi / 4, 1)
    result = x.tan()
    expected_real = math.tan(math.pi / 4)  # 1.0
    expected_dual = 1 / (math.cos(math.pi / 4) ** 2)  # 2.0
    assert math.isclose(result.real, expected_real, abs_tol=1e-9), "Dual tan real part incorrect."
    assert math.isclose(result.dual, expected_dual, abs_tol=1e-9), "Dual tan dual part incorrect."

    # Edge case: undefined tan (raises error for cos(x)=0)
    with pytest.raises(ValueError):
        x = Dual(math.pi / 2, 1)
        x.tan()

def test_exp():
    x = Dual(1, 1)
    result = x.exp()
    expected_real = math.exp(1)  # e ≈ 2.71828
    expected_dual = math.exp(1)  # derivative of exp is exp
    assert math.isclose(result.real, expected_real, abs_tol=1e-9), "Dual exp real part incorrect."
    assert math.isclose(result.dual, expected_dual, abs_tol=1e-9), "Dual exp dual part incorrect."

def test_log():
    x = Dual(math.exp(1), 1)
    result = x.log()
    expected_real = 1.0
    expected_dual = 1 / math.exp(1)
    assert math.isclose(result.real, expected_real, abs_tol=1e-9), "Dual log real part incorrect."
    assert math.isclose(result.dual, expected_dual, abs_tol=1e-9), "Dual log dual part incorrect."

    # Edge case: log of non-positive value (raises error)
    with pytest.raises(ValueError):
        x = Dual(-1, 1)
        x.log()

    with pytest.raises(ValueError):
        x = Dual(0, 1)
        x.log()

# ---------------------------
# Attribute Tests
# ---------------------------
def test_attribute_error_on_nonexistent_attribute():
    x = Dual(2, 1)
    with pytest.raises(AttributeError):
        value = x.non_existent_attribute

def test_attribute_error_on_nonexistent_method():
    x = Dual(2, 1)
    with pytest.raises(AttributeError):
        result = x.non_existent_method()

# ---------------------------
# Equality Tests
# ---------------------------
def test_equality():
    x = Dual(2, 1)
    y = Dual(2, 1)
    z = Dual(2, 0)
    assert x == y, "Dual instances with same real and dual parts should be equal."
    assert x != z, "Dual instances with different dual parts should not be equal."

    # Equality with scalar
    assert x != 2, "Dual instance should not be equal to scalar with different dual part."
    assert z != 2, "Dual instance should not be equal to scalar even if dual part is 0."

# ---------------------------
# Additional Exception Tests
# ---------------------------
def test_zero_real_and_dual():
    x = Dual(0, 0)
    with pytest.raises(ValueError):
        result = x.log()  # log(0) is undefined

def test_operation_with_none():
    x = Dual(2, 1)
    with pytest.raises(TypeError):
        result = x + None

    with pytest.raises(TypeError):
        result = x - None

    with pytest.raises(TypeError):
        result = x * None

    with pytest.raises(TypeError):
        result = x / None



def test_sinh():
    x = Dual(1, 1)
    result = x.sinh()
    assert math.isclose(result.real, math.sinh(1), abs_tol=1e-9)
    assert math.isclose(result.dual, math.cosh(1), abs_tol=1e-9)

# Test for cosh
def test_cosh():
    x = Dual(1, 1)
    result = x.cosh()
    assert math.isclose(result.real, math.cosh(1), abs_tol=1e-9)
    assert math.isclose(result.dual, math.sinh(1), abs_tol=1e-9)

# Test for tanh
def test_tanh():
    x = Dual(1, 1)
    result = x.tanh()
    assert math.isclose(result.real, math.tanh(1), abs_tol=1e-9)
    assert math.isclose(result.dual, 1 / (math.cosh(1) ** 2), abs_tol=1e-9)

# Test for arcsin
def test_arcsin():
    x = Dual(0.5, 1)  # Valid input
    result = x.arcsin()
    assert math.isclose(result.real, math.asin(0.5), abs_tol=1e-9)
    assert math.isclose(result.dual, 1 / math.sqrt(1 - 0.5**2), abs_tol=1e-9)

    # Invalid input (outside domain of arcsin)
    with pytest.raises(ValueError):
        x = Dual(1.5, 1)
        x.arcsin()

# Test for arccos
def test_arccos():
    x = Dual(0.5, 1)  # Valid input
    result = x.arccos()
    assert math.isclose(result.real, math.acos(0.5), abs_tol=1e-9)
    assert math.isclose(result.dual, -1 / math.sqrt(1 - 0.5**2), abs_tol=1e-9)

    # Invalid input (outside domain of arccos)
    with pytest.raises(ValueError):
        x = Dual(-1.5, 1)
        x.arccos()

# Test for arctan
def test_arctan():
    x = Dual(1, 1)
    result = x.arctan()
    assert math.isclose(result.real, math.atan(1), abs_tol=1e-9)
    assert math.isclose(result.dual, 1 / (1 + 1**2), abs_tol=1e-9)

# Test for logarithm with arbitrary base
def test_log():
    x = Dual(math.e, 1)  # Valid input
    result = x.log(base=math.e)
    assert math.isclose(result.real, math.log(math.e), abs_tol=1e-9)
    assert math.isclose(result.dual, 1 / math.e, abs_tol=1e-9)

    # Invalid input (non-positive value)
    with pytest.raises(ValueError):
        x = Dual(0, 1)
        x.log()

    with pytest.raises(ValueError):
        x = Dual(-1, 1)
        x.log()

# Test for power
def test_power():
    x = Dual(2, 1)  # Valid input
    result = x.power(3)
    assert math.isclose(result.real, 8, abs_tol=1e-9)
    assert math.isclose(result.dual, 12, abs_tol=1e-9)  # Derivative = 3 * 2^2 = 12

# Test for root
def test_root():
    # Valid input
    x = Dual(9, 1)
    result = x.root(2)  # Square root
    assert math.isclose(result.real, 3, abs_tol=1e-9)
    assert math.isclose(result.dual, 1 / (2 * 3), abs_tol=1e-9)  # Derivative = 1 / (2 * sqrt(9))

    # Invalid input (negative number for even root)
    with pytest.raises(ValueError):
        x = Dual(-9, 1)
        x.root(2)



