"""Python bindings for zigmath library."""

import ctypes
import os
import platform
import sys
from pathlib import Path

__all__ = ["ZigMath", "add", "factorial"]


def _get_library_name() -> str:
    """Determine the correct library filename based on platform."""
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == "darwin":  # macOS
        if machine == "arm64":
            return "libzigmath_arm64.dylib"
        else:
            return "libzigmath_x64.dylib"
    elif system == "linux":
        return "libzigmath_x64.so"
    else:
        raise RuntimeError(f"Unsupported platform: {system}")


def _find_library() -> Path:
    """Find the zigmath library file."""
    lib_name = _get_library_name()
    
    # Check relative to Python module first
    module_dir = Path(__file__).parent
    lib_path = module_dir.parent / lib_name
    if lib_path.exists():
        return lib_path
    
    # Check in same directory as module
    lib_path = module_dir / lib_name
    if lib_path.exists():
        return lib_path
    
    # Check in current working directory
    lib_path = Path(lib_name)
    if lib_path.exists():
        return lib_path
    
    raise FileNotFoundError(
        f"Could not find {lib_name}. "
        f"Make sure the library is built and in the correct location."
    )


class ZigMath:
    """Python interface to the zigmath library."""
    
    def __init__(self) -> None:
        """Initialize the ZigMath interface."""
        lib_path = _find_library()
        try:
            self._lib = ctypes.CDLL(str(lib_path))
        except OSError as e:
            raise RuntimeError(f"Failed to load library {lib_path}: {e}") from e
        
        self._setup_functions()
    
    def _setup_functions(self) -> None:
        """Configure function signatures and return types."""
        # int add(int a, int b)
        self._lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
        self._lib.add.restype = ctypes.c_int
        
        # int64_t factorial(int n)
        self._lib.factorial.argtypes = [ctypes.c_int]
        self._lib.factorial.restype = ctypes.c_int64
    
    def add(self, a: int, b: int) -> int:
        """Add two integers."""
        return self._lib.add(a, b)
    
    def factorial(self, n: int) -> int:
        """Compute factorial of n. Returns -1 for negative input."""
        return self._lib.factorial(n)


# Create a global instance for convenience functions
_zigmath = None


def _get_zigmath() -> ZigMath:
    """Get or create the global ZigMath instance."""
    global _zigmath
    if _zigmath is None:
        _zigmath = ZigMath()
    return _zigmath


def add(a: int, b: int) -> int:
    """Add two integers using the zigmath library."""
    return _get_zigmath().add(a, b)


def factorial(n: int) -> int:
    """Compute factorial using the zigmath library."""
    return _get_zigmath().factorial(n)