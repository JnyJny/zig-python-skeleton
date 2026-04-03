#!/usr/bin/env python3
"""Manual test script for zigmath library."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'python'))

from zigmath import ZigMath, add, factorial

def test_add():
    """Test add function."""
    print("Testing add function...")
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    assert add(100, -50) == 50
    print("  add tests passed!")

def test_factorial():
    """Test factorial function."""
    print("Testing factorial function...")
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    assert factorial(6) == 720
    assert factorial(-1) == -1
    assert factorial(-5) == -1
    print("  factorial tests passed!")

def test_class_interface():
    """Test ZigMath class interface."""
    print("Testing ZigMath class...")
    zm = ZigMath()
    assert zm.add(10, 20) == 30
    assert zm.factorial(4) == 24
    print("  ZigMath class tests passed!")

def main():
    """Run all tests."""
    print("Running manual tests for zigmath library...")
    try:
        test_add()
        test_factorial()
        test_class_interface()
        print("\nAll tests passed!")
        return 0
    except Exception as e:
        print(f"\nTest failed: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())