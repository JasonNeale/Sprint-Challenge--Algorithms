'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    # check if word has been assigned a value
    if not word:
        # if not then return 0
        return 0
    # if word has been assigned a value then continue
    else:
        # checks for "th" within the word
        if word[:2] == "th":
            # found "th", count = 1
            count = 1
        else:
            # didn't find "th", count = 0
            count = 0
        
        # return the count plus the count of the recursion
        return count + count_th(word[1:])

print(count_th("the")) #returns 1
print(count_th("thethe")) #return 2
print(count_th("thethethe")) #returns 3