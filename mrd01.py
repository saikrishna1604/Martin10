# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 19:13:16 2018
Answer for Mission R&D Question number 1
@author: Prasad Siri
"""


def summation_of_ordinal_value(str_input):
    ret = 0
    for j in range(0, len(str_input)):
        ret = ret + ord(str_input[j])
    return ret


def mirror_build(initial_char, seq):
    start = ord(initial_char)
    end = start + seq
    for j in range(start, end):
        mirror.update({chr(j): chr(end - 1 + start - j)})


initial_input = "Abtrur56 kdkajh4647 dsffsh9"
print(initial_input)

# Building Mirror Dictionary
mirror = {}
mirror_build("A", 26)
mirror_build("a", 26)
mirror_build("0", 10)
mirror.update({" ": " "})
print(mirror)


# Building output string based on mirror dictionary
output = ""
for i in range(0, len(initial_input)):
    each_chr = mirror.get(initial_input[i])
    output = output + each_chr
print(output)

# Build output_list by splitting single string
# into multiple word being space as separator
output_list = output.split()
print(output_list)

# Find Ordinal Value of each character and summation of the values
# and build dictionary summation ordinal value as key and string as value pair
output_ordinal_summation_value_list = []
output_dictionary = {}
for i in range(0, len(output_list)):
    sov = summation_of_ordinal_value(output_list[i])
    output_ordinal_summation_value_list.append(sov)
    output_dictionary.update({sov: output_list[i]})
print(output_ordinal_summation_value_list)
print(output_dictionary)

# Building descending ordered list
descending_output_keys = sorted(output_ordinal_summation_value_list, reverse=True)
print(descending_output_keys)

# Building final output based on dictionary built on previous step
final_output_list = []
for i in range(0, len(descending_output_keys)):
    final_output_list.append(output_dictionary.get(descending_output_keys[i]))
print(final_output_list)
