

"""
Exercise: Retry Simulation
Student: Milan Shrestha
Day: 2
"""


import random

# --- Configuration ---
attempt = 1                    # Track the current attempt number (starts at 1, not 0, for human-readable output)
max_attempts = 3               # Maximum number of retries allowed before giving up
operation_successful = False   # Tracks outcome; drives both the early exit and the final message

# --- Retry loop ---
# Runs until either max_attempts is reached OR the operation succeeds (via break)
while attempt <= max_attempts:
    print(f"Attempt {attempt}")

    # Stretch: simulate success on the 2nd attempt specifically (deterministic, easy to test)
    # Swap this line for `random.random() < 0.5` if you want randomized success instead
    operation_successful = (attempt == 2)

    if operation_successful:
        break  # Exit immediately — no point burning remaining attempts once we've succeeded

    attempt += 1  # Only increment on failure; a successful attempt breaks before reaching this line

# --- Final result ---
# Runs once, after the loop ends (either by break or by exhausting max_attempts)
print("Operation completed successfully" if operation_successful else "Operation failed after three attempts")