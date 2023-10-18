def minion_game(string):
    # your code goes here
    vowels = set('AEIOU') # Using set is faster than tuple
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += (len(s)-i)
        else:
            stuart += (len(s)-i)

    if kevin > stuart:
        print ("{} {}".format("Kevin",kevin))
    elif kevin < stuart:
        print ("{} {}".format("Stuart",stuart))
    else:
        print ("Draw")