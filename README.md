# zig-python-skeleton

A skeleton for Python packages that call into Zig implementations via C ABI.

## Overview

This project demonstrates how to create a Python package that calls functions
implemented in Zig through a C-compatible interface. The Zig code is compiled
to a shared library that Python loads via ctypes.

## Structure

```
├── src/
│   └── zigmath.zig         # Zig implementation with C exports
├── python/
│   ├── zigmath.py          # Python bindings via ctypes
│   ├── test_zigmath.py     # Python tests
│   └── setup.py            # Python package setup
├── build.zig               # Zig build configuration
├── Makefile                # Build automation
└── README.md
```

## Building

### Prerequisites

- Zig 0.15.x or later
- Python 3.8 or later
- make (optional, for convenience)

### Quick Start

1. Build the Zig library:
   ```bash
   make build
   ```

2. Install the Python package:
   ```bash
   make install
   ```

3. Run tests:
   ```bash
   make test
   ```

### Manual Build Steps

1. Build Zig libraries for your platform:
   ```bash
   # For macOS
   zig build-lib -dynamic -lc -target aarch64-macos src/zigmath.zig \
       -femit-bin=libzigmath_arm64.dylib

   # For Linux
   zig build-lib -dynamic -lc -target x86_64-linux-gnu src/zigmath.zig \
       -femit-bin=libzigmath_x64.so
   ```

2. Install Python package:
   ```bash
   cd python
   pip install -e .
   ```

3. Run tests:
   ```bash
   cd python
   python -m pytest test_zigmath.py -v
   ```

## Usage

```python
from zigmath import add, factorial

# Use convenience functions
result = add(2, 3)          # Returns 5
fact = factorial(5)         # Returns 120

# Or use the class interface
from zigmath import ZigMath

zm = ZigMath()
result = zm.add(10, 20)
fact = zm.factorial(6)
```

## Implementation Details

### Zig Side

The Zig implementation exports functions with C ABI:

```zig
export fn add(a: i32, b: i32) i32 {
    return a + b;
}

export fn factorial(n: i32) i64 {
    // Implementation
}
```

### Python Side

Python bindings use ctypes to call the shared library:

```python
import ctypes

lib = ctypes.CDLL("libzigmath.so")
lib.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib.add.restype = ctypes.c_int
```

## Cross-Platform Support

The skeleton supports multiple platforms by building different library files:

- macOS ARM64: `libzigmath_arm64.dylib`
- macOS x64: `libzigmath_x64.dylib`
- Linux x64: `libzigmath_x64.so`

The Python bindings automatically detect the platform and load the correct
library file.

## Testing

The project includes comprehensive tests:

- Zig tests: `zig test --test-no-exec src/zigmath.zig`
- Python tests: `python -m pytest test_zigmath.py`

## Future Directions

This skeleton can be extended to:

- Add more complex data types (structs, arrays)
- Use cffi instead of ctypes for better performance
- Add Windows support (.dll files)
- Integrate with Python packaging tools for distribution
- Add memory management for complex data structures
- Implement async/callback interfaces

*Authored by Jny*