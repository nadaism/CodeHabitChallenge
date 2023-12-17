"""
Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (true means present).

The correct answer would be 17.
Hint: Don't forget to check for bad values like null/undefined
"""

def count_sheeps(sheep):
    if not sheep:
        return 0
    
    jumlah_domba=0
    for i in sheep:
        if i == True:
            jumlah_domba += 1
            
    return jumlah_domba