def concat_upper(str1,str2):
    return (str1 + " " + str2).upper()

# Using variables
str1 = "tarun"
str2 = "kotagiri"

print(concat_upper(str1,str2))

# Without using variables
print(concat_upper("Tarun",concat_upper(str1,str2)))

print(concat_upper(str1,concat_upper("Tarun",concat_upper(str1,str2))))