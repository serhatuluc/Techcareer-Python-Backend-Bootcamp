def remove_space(text):
    new_text = ""
    for char in text:
        if char == " ":
            continue
        else:
            new_text += char
    return new_text
    
print(remove_space("Hey, hope you are doing good"))