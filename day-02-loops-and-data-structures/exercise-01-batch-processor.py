
"""
Exercise: Batch Processor
Student: Milan Shrestha
Day: 2
"""

# Process 10 batches sequentially (batch numbers 1 through 10)
for batch_number_val in range(1,11):
    print(f"Processing batch {batch_number_val}")

# Save a checkpoint every 3rd batch to allow recovery without reprocessing everything
    if(batch_number_val %3 ==0):
        print("Checkpoint reached")