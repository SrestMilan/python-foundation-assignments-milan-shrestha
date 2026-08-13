

raw_values = [100, None, 250, "invalid", 300, None, 450]

clean_value_list = []  # will hold only the values that pass the integer check

for x in raw_values:
    # Skip anything that isn't a true integer (filters out None, strings, etc.)
    if not isinstance(x, int): continue
    clean_value_list.append(x)  # only reached when x IS an integer

print(f"The new list containing value :{clean_value_list}")



#List comprehension
raw_values = [100, None, 250, "invalid", 300, None, 450]

# Build a new list keeping only true integers;
# isinstance(x, int) acts as the comprehension's filter — same result as the loop + continue version, just condensed
clean_value_list = [x for x in raw_values if isinstance(x, int)]

print(f"The new list containing value :{clean_value_list}")