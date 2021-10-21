#!/usr/bin/python3
""" Text indentation """


def text_indentation(text):
    """ function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    space = 0
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i, j in enumerate(text):
        if j in '.?:':
            print(text[space: i + 1].strip() + '\n')
            space = i + 1
    if space < len(text):
        print(text[space:].strip(), end="")
