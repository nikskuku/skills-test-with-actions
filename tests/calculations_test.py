# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import area_of_circle, get_nth_fibonacci   # noqa: E402


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - 3.14159) < 1e-5


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


# def test_get_nth_fibonacci_ten():
#     """Test with n=10."""
#     # Arrange
#     n = 10

#     # Act
#     result = get_nth_fibonacci(n)

#     # Assert
#     assert result == 89

# tests/test_calculations.py
import pytest
from src.calculations import area_of_circle, get_nth_fibonacci


class TestAreaOfCircle:
    def test_area_of_circle_positive(self):
        """Test area calculation with positive radius."""
        assert area_of_circle(5) == pytest.approx(78.54, abs=0.01)
    
    def test_area_of_circle_zero(self):
        """Test area calculation with zero radius."""
        assert area_of_circle(0) == 0
    
    def test_area_of_circle_negative(self):
        """Test that negative radius raises ValueError."""
        with pytest.raises(ValueError, match="Radius cannot be negative"):
            area_of_circle(-5)


class TestGetNthFibonacci:
    def test_fibonacci_zero(self):
        """Test fibonacci(0)."""
        assert get_nth_fibonacci(0) == 0
    
    def test_fibonacci_one(self):
        """Test fibonacci(1)."""
        assert get_nth_fibonacci(1) == 1
    
    def test_fibonacci_sequence(self):
        """Test fibonacci sequence."""
        assert get_nth_fibonacci(6) == 8
        assert get_nth_fibonacci(10) == 55
    
    def test_fibonacci_negative(self):
        """Test that negative n raises ValueError."""
        with pytest.raises(ValueError, match="n cannot be negative"):
            get_nth_fibonacci(-1)
