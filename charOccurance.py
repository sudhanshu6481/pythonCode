def char_occur(string):
    char_count = {}
    for char in string:
        if char != " ":
            if char not in char_count:
                count_of_char = string.count(char)
                char_count[char] = count_of_char
    return char_count

string = 'Hello world'
x = char_occur(string)
print(x)
