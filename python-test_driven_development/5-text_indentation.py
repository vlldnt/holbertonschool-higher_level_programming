#!/usr/bin/python3
def text_indentation(text):
    '''
    Function that print /n after '.' '?' ':'
    text : the text to indentate
    Print the new text
    '''

    new_text = ""
    i = 0
    delim = ['?', '.', ':']

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    while i < len(text):
        new_text += text[i]
        if text[i] in delim:
            new_text += "\n\n"
            i += 1
            while (i < len(text) and text[i] == ' '):
                i += 1
        i += 1

    print("{:s}".format(new_text), end="")
