"""
temperature_utils.py

A small utility module for converting between Celsius and Fahrenheit.
"""

MODULE_VERSION = "1.0"


def celsius_to_fahrenheit(c):
    """Convert a Celsius temperature to Fahrenheit."""
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    """Convert a Fahrenheit temperature to Celsius."""
    return (f - 32) * 5 / 9