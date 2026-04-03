"""Python wrapper for Zig math functions.

Provides Python bindings to Zig-implemented mathematical functions
via ctypes and a shared library.
"""
import ctypes
import os
from pathlib import Path
from typing import Union


class ZigMath:
    """Wrapper for Zig math library functions."""
    
    def __init__(self, lib_path: Union[str, Path, None] = None):
        """Initialize the wrapper with the shared library.
        
        Args:
            lib_path: Path to the Zig shared library. If None, looks for
                     libzigmath.dylib in the same directory as this module.
        """
        if lib_path is None:
            lib_path = Path(__file__).parent / "libzigmath.dylib"
        
        if not Path(lib_path).exists():
            raise FileNotFoundError(f"Zig library not found at {lib_path}")
        
        self._lib = ctypes.CDLL(str(lib_path))
        self._setup_function_signatures()
    
    def _setup_function_signatures(self):
        """Configure ctypes function signatures for type safety."""
        # add_numbers(i32, i32) -> i32
        self._lib.add_numbers.argtypes = [ctypes.c_int32, ctypes.c_int32]
        self._lib.add_numbers.restype = ctypes.c_int32
        
        # multiply_floats(f64, f64) -> f64
        self._lib.multiply_floats.argtypes = [ctypes.c_double, ctypes.c_double]
        self._lib.multiply_floats.restype = ctypes.c_double
        
        # factorial(i32) -> i64
        self._lib.factorial.argtypes = [ctypes.c_int32]
        self._lib.factorial.restype = ctypes.c_int64
    
    def add(self, a: int, b: int) -> int:
        """Add two integers.
        
        Args:
            a: First integer
            b: Second integer
            
        Returns:
            Sum of a and b
        """
        return self._lib.add_numbers(a, b)
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two floats.
        
        Args:
            a: First float
            b: Second float
            
        Returns:
            Product of a and b
        """
        return self._lib.multiply_floats(a, b)
    
    def factorial(self, n: int) -> int:
        """Calculate factorial of a number.
        
        Args:
            n: Non-negative integer
            
        Returns:
            Factorial of n, or -1 for invalid input
        """
        return self._lib.factorial(n)


# Convenience instance for direct use
_default_instance = None


def get_math() -> ZigMath:
    """Get the default ZigMath instance."""
    global _default_instance
    if _default_instance is None:
        _default_instance = ZigMath()
    return _default_instance


def add(a: int, b: int) -> int:
    """Add two integers using Zig implementation."""
    return get_math().add(a, b)


def multiply(a: float, b: float) -> float:
    """Multiply two floats using Zig implementation."""
    return get_math().multiply(a, b)


def factorial(n: int) -> int:
    """Calculate factorial using Zig implementation."""
    return get_math().factorial(n)