#!/usr/bin/python3
def remove_char_at(str, n):
    str1 = str
    if n >= 0 and n < len(str):
        str1 = str.replace(str[n], "")
    return str1
