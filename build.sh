#!/bin/bash
# Build script for Zig-Python skeleton

set -e

echo "Building Zig shared library..."
zig build-lib -target aarch64-macos -dynamic lib.zig

echo "Renaming library to libzigmath.dylib..."
mv liblib.dylib libzigmath.dylib

echo "Testing Python bindings..."
python3 -c "import zigmath; print('Build test: 5 + 3 =', zigmath.add(5, 3))"

echo "Build complete!"