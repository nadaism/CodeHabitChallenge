"""
Write a function to convert a name into initials. 
This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:
    Sam Harris => S.H
    patrick feeney => P.F
"""
def abbrev_name(name):
    name = name.upper()
    name_part = name.split()
    first_word = name_part[0][0]
    second_word = name_part[1][0]
    return f"{first_word}.{second_word}"