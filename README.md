# Zig-Python Skeleton

A skeleton project demonstrating how to build Python packages that call into Zig implementations via shared libraries.

## What This Does

- **Zig side**: Compiles Zig functions to a C-ABI shared library
- **Python side**: Uses ctypes to call Zig functions from Python  
- **Examples**: Basic math functions (add, multiply, factorial)
- **Tests**: Full pytest suite proving everything works

## Quick Start

```bash
# Build the Zig shared library
./build.sh

# Run tests
python3 -m pytest test_zigmath.py -v

# Use it
python3 -c "import zigmath; print(zigmath.factorial(10))"
```

## Requirements

- **Zig 0.15.2** (tested version)
- **Python 3.7+** with pytest
- **macOS** (aarch64, but easily adaptable)

## Architecture

### Zig Library (`lib.zig`)

Defines C-ABI functions using the `export` keyword:

```zig
export fn add_numbers(a: i32, b: i32) i32 {
    return a + b;
}
```

### Python Wrapper (`zigmath.py`) 

Uses ctypes to load the shared library and call functions:

```python
self._lib.add_numbers.argtypes = [ctypes.c_int32, ctypes.c_int32]
self._lib.add_numbers.restype = ctypes.c_int32
```

### Build Process

1. `zig build-lib -target aarch64-macos -dynamic lib.zig`
2. Produces `liblib.dylib` → renamed to `libzigmath.dylib`
3. Python imports and loads via ctypes.CDLL()

## Files

- `lib.zig` - Zig source with C-ABI exports
- `zigmath.py` - Python ctypes wrapper
- `test_zigmath.py` - Test suite  
- `build.sh` - Build script
- `libzigmath.dylib` - Compiled shared library

## Testing

```bash
python3 -m pytest test_zigmath.py -v
```

Tests cover:
- Basic functionality (add, multiply, factorial)
- Edge cases (zero, negative numbers) 
- Both direct function calls and class interface
- Error handling (missing library)

## Extending

To add new functions:

1. Add `export fn` to `lib.zig`
2. Rebuild: `./build.sh` 
3. Add Python wrapper method to `zigmath.py`
4. Configure ctypes signature in `_setup_function_signatures()`
5. Add tests to `test_zigmath.py`

## Platform Notes

This skeleton targets aarch64 macOS. For other platforms:

- **Linux**: Change target to `x86_64-linux` or `aarch64-linux`
- **Windows**: Use `.dll` extension, adjust ctypes loading
- **Cross-compilation**: Zig handles most targets out of the box

---

**Authored by Jny**