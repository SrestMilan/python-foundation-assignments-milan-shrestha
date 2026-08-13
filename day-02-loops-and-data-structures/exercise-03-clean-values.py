

raw_values = [100, None, 250, "invalid", 300, None, 450]
clean_value_list=[]
for x in raw_values:
    if not isinstance(x,int):continue
    clean_value_list.append(x)

print(f"The new list containing value :{clean_value_list}")
