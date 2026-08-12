"""
Exercise: Pipeline Health Status
Student: Milan Shrestha
Day: 1
"""
# Total records loaded and how many failed during the pipeline run
rows_loaded = 9800
rows_failed = 200
runtime_minutes = 18

# Calculate failure rate as a percentage
failure_rate = (rows_failed / rows_loaded) * 100

# Healthy: failure rate <= 2% AND runtime <= 20 minutes (both required)
if failure_rate <= 2 and runtime_minutes <= 20:
    status = "Healthy"
# Reached only if NOT healthy - so either failure rate > 2%, or runtime > 20 min (or both)
# If failure rate is still <= 5% here, classify as Warning
elif failure_rate <= 5:
    status = "Warning"
# Otherwise failure rate must be > 5%
else:
    status = "Critical"

# Display results
print(f"Failure Rate: {failure_rate:.2f}%")
print(f"Pipeline Status: {status}")