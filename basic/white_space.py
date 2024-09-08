#!/usr/bin/env python

print()
strings = ["     Filet Migon", "Brisket    ", "   Cheesseburger    "]

combined_string_length = 0
for string in strings:
    print(string)
    print(len(string))
    combined_string_length += len(string)
    
print("Combined String Length: ", combined_string_length)

combined_string_length = 0
print()
for string in strings:
    string = string.strip()
    print(string)
    combined_string_length += len(string)

print("Combined String Length: ", combined_string_length)
