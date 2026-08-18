# Day 3 — Functions and Modules

## Overview

This folder contains my Day 3 Python assignments focused on **Functions and Modules**.

The exercises cover default arguments, `*args`, built-in functions, multiple return values, variable scope, the `global` keyword, custom modules, and Python's standard library modules.

## Topics Covered

* Functions with default arguments
* Variable-length arguments using `*args`
* Built-in functions: `min()`, `max()`, `sum()`, and `sorted()`
* Multiple return values
* Global variables and the `global` keyword
* Creating and importing custom Python modules
* Using the `random` module
* Using the `datetime` module

## Exercises

### Question 1 — Simple Interest Calculator

Created a `calculate_simple_interest()` function using default arguments for the interest rate and time.

Formula:

```text
Interest = (Principal × Rate × Time) / 100
```

### Question 2 — Class Average

Created a `class_average()` function using `*args` to accept any number of scores.

The function calculates the average and returns `0` when no scores are provided.

### Question 3 — Analyze Numbers

Created an `analyze_numbers()` function that returns:

1. Smallest number
2. Largest number
3. Sum of all numbers
4. Numbers sorted in descending order

The solution uses Python's built-in `min()`, `max()`, `sum()`, and `sorted()` functions.

### Question 4 — Shared Booking Counter

Created a simple booking system using a global variable called `total_seats_booked`.

The `book_seats()` function increases the total number of booked seats, while `reset_bookings()` resets the counter to zero.

Both functions demonstrate the use of the `global` keyword.

### Question 5 — Temperature Report Module

Created a custom module named `temperature_utils.py`.

The module contains:

* `celsius_to_fahrenheit()`
* `fahrenheit_to_celsius()`
* `MODULE_VERSION`

The notebook also uses the `random` module to generate Celsius temperatures and the `datetime` module to display the current date.

## Files

```text
day-03/
│
├── functions_and_modules.ipynb
└── temperature_utils.py
```

## Key Learning

Through these exercises, I practiced creating reusable functions, working with different types of function arguments, managing variable scope, returning multiple values, and creating custom Python modules.

## Status

* [x] Question 1 — Simple Interest Calculator
* [x] Question 2 — Class Average
* [x] Question 3 — Analyze Numbers
* [x] Question 4 — Shared Booking Counter
* [x] Question 5 — Temperature Report Module
