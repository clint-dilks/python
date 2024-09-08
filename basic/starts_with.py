#!/usr/bin/env python

print()
strings = ['Becomes', 'becomes', 'BEAR', '    bEautiful']

print("RAW:", "\n")

for word in strings:
    print(word.startswith('be'))

print()
print("Case Insensitive, whitespace stripped:") 
print()

for word in strings:
    word = word.strip()
    word = word.lower()
    print(word.startswith('be'))