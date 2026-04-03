"""Tests for zigmath Python bindings."""

import pytest
from zigmath import ZigMath, add, factorial


class TestZigMath:
    """Test the ZigMath class."""
    
    def test_add(self) -> None:
        """Test the add function."""
        zm = ZigMath()
        assert zm.add(2, 3) == 5
        assert zm.add(-1, 1) == 0
        assert zm.add(0, 0) == 0
        assert zm.add(100, -50) == 50
    
    def test_factorial(self) -> None:
        """Test the factorial function."""
        zm = ZigMath()
        assert zm.factorial(0) == 1
        assert zm.factorial(1) == 1
        assert zm.factorial(5) == 120
        assert zm.factorial(6) == 720
        assert zm.factorial(-1) == -1
        assert zm.factorial(-5) == -1


class TestConvenienceFunctions:
    """Test the convenience functions."""
    
    def test_add_function(self) -> None:
        """Test the convenience add function."""
        assert add(2, 3) == 5
        assert add(-1, 1) == 0
        assert add(0, 0) == 0
    
    def test_factorial_function(self) -> None:
        """Test the convenience factorial function."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(-1) == -1


class TestEdgeCases:
    """Test edge cases and error conditions."""
    
    def test_large_numbers(self) -> None:
        """Test with larger numbers."""
        zm = ZigMath()
        assert zm.add(1000000, 2000000) == 3000000
        assert zm.factorial(10) == 3628800
    
    def test_type_handling(self) -> None:
        """Test that Python types are handled correctly."""
        zm = ZigMath()
        
        # These should work (Python int -> C int)
        assert zm.add(1, 2) == 3
        assert zm.factorial(5) == 120
        
        # Test with bool (should convert to int)
        assert zm.add(True, False) == 1
        assert zm.add(True, True) == 2