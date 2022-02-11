def getCompressedString(input):
    new_string = ""
    prev_char = input[0]
    count = 1

    for i in range(1, len(input)):
        if input[i] == prev_char:
            count += 1
        else:
            new_string += prev_char + (str(count) if count > 1 else "")
            prev_char = input[i]
            count = 1
    
    new_string += input[-1] + (str(count) if count > 1 else "")
    
    return new_string
