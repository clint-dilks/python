#!/usr/bin/env python

user_input = ''
while user_input == '':
    user_input = input("Tell me your password:")
print('The first letter you entered was:', user_input[0].upper())