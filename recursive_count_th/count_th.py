'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    th = "th"

    if(len(word) == 0 or len(word) < 2):
        return 0
    if(word[0:len(th)] == th):
        return count_th(word[len(th) - 1:]) + 1
    return count_th(word[len(th) - 1:])
