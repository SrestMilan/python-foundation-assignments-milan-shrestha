
"""
Exercise: Dataset Comparison
Student: Milan Shrestha
Day: 2
"""



dataset_a = {
    "customer",
    "sales",
    "product",
    "employee"
}

dataset_b = {
    "sales",
    "product",
    "supplier",
    "inventory"
}

# All unique dataset names across both groups (union removes duplicates automatically)
total_datasets = dataset_a | dataset_b

# Datasets that appear in both groups (intersection)
common_item_datasets = dataset_a & dataset_b

# Datasets found only in dataset_a, not in dataset_b (difference)
only_in_a = dataset_a - dataset_b

# Datasets found only in dataset_b, not in dataset_a (difference)
only_in_b = dataset_b - dataset_a

print(f"All unique datasets: {total_datasets}")
print(f"Common to both datasets: {common_item_datasets}")
print(f"Only in dataset_a: {only_in_a}")
print(f"Only in dataset_b: {only_in_b}")