"""Tests for Zig math function bindings."""
import pytest
import zigmath


def test_add_positive_numbers():
    """Test addition with positive integers."""
    result = zigmath.add(5, 3)
    assert result == 8


def test_add_negative_numbers():
    """Test addition with negative integers."""
    result = zigmath.add(-5, -3)
    assert result == -8


def test_add_mixed_signs():
    """Test addition with mixed positive and negative."""
    result = zigmath.add(10, -3)
    assert result == 7


def test_add_with_zero():
    """Test addition with zero."""
    result = zigmath.add(42, 0)
    assert result == 42


def test_multiply_positive_floats():
    """Test multiplication with positive floats."""
    result = zigmath.multiply(2.5, 4.0)
    assert result == 10.0


def test_multiply_negative_floats():
    """Test multiplication with negative floats."""
    result = zigmath.multiply(-2.5, -4.0)
    assert result == 10.0


def test_multiply_mixed_sign_floats():
    """Test multiplication with mixed signs."""
    result = zigmath.multiply(-2.5, 4.0)
    assert result == -10.0


def test_multiply_with_zero():
    """Test multiplication with zero."""
    result = zigmath.multiply(42.7, 0.0)
    assert result == 0.0


def test_factorial_small_numbers():
    """Test factorial of small positive numbers."""
    assert zigmath.factorial(0) == 1
    assert zigmath.factorial(1) == 1
    assert zigmath.factorial(2) == 2
    assert zigmath.factorial(3) == 6
    assert zigmath.factorial(4) == 24
    assert zigmath.factorial(5) == 120


def test_factorial_larger_number():
    """Test factorial of larger number."""
    result = zigmath.factorial(10)
    assert result == 3628800


def test_factorial_negative_number():
    """Test factorial with negative input returns error."""
    result = zigmath.factorial(-5)
    assert result == -1


@pytest.fixture
def math_instance():
    """Fixture providing a ZigMath instance."""
    return zigmath.ZigMath()


def test_class_interface_add(math_instance):
    """Test class interface for addition."""
    result = math_instance.add(7, 13)
    assert result == 20


def test_class_interface_multiply(math_instance):
    """Test class interface for multiplication."""
    result = math_instance.multiply(3.5, 2.0)
    assert result == 7.0


def test_class_interface_factorial(math_instance):
    """Test class interface for factorial."""
    result = math_instance.factorial(6)
    assert result == 720


def test_library_not_found():
    """Test error handling when library file is missing."""
    with pytest.raises(FileNotFoundError):
        zigmath.ZigMath("/nonexistent/path.dylib")