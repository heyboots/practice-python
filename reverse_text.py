def reverse(text):
    char = len(text) - 1                # gets length of string and sets as char - 1
    reverse_text = []                   # creates empty list
    for x in range(1, len(text) + 1):   # Loops through an arbitrially long string
        reverse_text.append(text[char]) # Takes character at location char in string and appends to end of reverse_text
        char -= 1                       # subtracts char by one to work backward through string
    return ''.join(reverse_text)        # joins list to remove whitespace
