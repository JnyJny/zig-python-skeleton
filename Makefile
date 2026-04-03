# Makefile for zig-python-skeleton

.PHONY: all clean build test install build-lib build-macos build-linux

all: build

build: build-macos build-linux

build-lib: build

build-macos:
	zig build-lib -dynamic -lc -target aarch64-macos src/zigmath.zig -femit-bin=libzigmath_arm64.dylib
	zig build-lib -dynamic -lc -target x86_64-macos src/zigmath.zig -femit-bin=libzigmath_x64.dylib

build-linux:
	zig build-lib -dynamic -lc -target x86_64-linux-gnu src/zigmath.zig -femit-bin=libzigmath_x64.so

test:
	zig test -target x86_64-linux-gnu --test-no-exec src/zigmath.zig
	python test_manual.py

install:
	cd python && pip install -e .

clean:
	rm -rf zig-cache zig-out .zig-cache *.so *.dylib
	cd python && rm -rf build dist *.egg-info __pycache__ .pytest_cache