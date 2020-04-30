def decodeString(self, s: str) -> str:
    """
    String contains encoded data in the format k[string],
    where k is how many times [string] is to be repeated
    
    
    Example:
        5[e]2[bc]10[a]
        
        decodes to:
        eeeeebcbcaaaaaaaaaa
    
    #1 
    make a string for the decoded message
    
    enter a while loop to parse the provided s str
    read until opening bracket is encountered, this is the number k
    store this in k
    read until closing bracket is found, this is the string to repeat

    Append message to decoded string by multiplying chars by k
    decoded_message += (chars * int(k))
    - Failed
    
    #2 
    String to hold resulting decoded message
    
    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
    
    Unique terms
    numbers -> specify how many times to repeat the FOLLOWING chars in square brackets
    square brackets -> Signify chars to be repeated
    letters -> by themselves mean append to message, don't repeat them
    
    while loop to iterate over each character in a string
    
    booleans to set the "mode" of parsing?
    
    If the char is a number, use it as repeatedTimes
    Read the following chars until closing bracket.?
    This will be the message we repeat k times
    append k repeated message to decoded_message,
    continue....
    If char is not a number or a square bracket or we aren't inside a square bracket, then its just
    a letter to be appended to decoded_message
    
    edge case of 2[a3[c]] (nested commands...)
    - unknown at this time...
    
    """
    decoded_message = ""

    repeated_times = 1
    repeated_string = ""
    repeat_mode = False

    for c in s:
        if c.isdigit():
            # Get digit, enter repeat mode
            repeated_times = int(c)
            repeat_mode = True

        elif repeat_mode:
            # any chars encountered will be part of repeated_string
            # except for numbers or brackets
            if c != "]":
                if c != "[":
                    repeated_string += c
            else:
                # Append correctly multiplied string to decoded_message
                decoded_message += repeated_string * repeated_times

                # Reset
                repeated_times = 1
                repeated_string = ""
                repeat_mode = False
        else:
            # A char by itself, not in brackets, and not an integer
            decoded_message += c

    return decoded_message


"""
Works with 2/3 cases

Examples:

s = "3[a]2[bc]", return "aaabcbc". ✔
s = "3[a2[c]]", return "accaccacc". ❌
s = "2[abc]3[cd]ef", return "abcabccdcdcdef". ✔
"""
