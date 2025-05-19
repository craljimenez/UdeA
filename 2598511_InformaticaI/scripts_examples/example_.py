def fragmentar(text,w=" "):
    word_text = ""
    word = ""
    l = 0
    for char in text:
        if char != w:
            word = word + char
        else:
            word_text = word_text + word + "\n"
            l = l + 1
            word = ""
    
    if char != w:
        word_text = word_text + word + "\n"
        l = l + 1
    print("l = ",l)
    return word_text


paragraph = "Strings are inmutable data objects in Python"
w = "|"
print(fragmentar(paragraph,"n"))

