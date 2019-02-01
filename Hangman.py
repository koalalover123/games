def hangman(count):
    if count == 1:
        print ("O")
    if count == 2:
        print ("O")
        print ("|")
        print ("|")
    if count == 3:
        print  ("O")
        print ("\|")
        print  ("|")
    if count == 4:
        print  ("O")
        print ("\|/")
        print  ("|")
    if count == 5:
        print  ("O")
        print ("\|/")
        print ("/|")
    if count == 6:
        print  (" O ")
        print  ("\|/")
        print  ("/|\  ")
        print ("you loose")
        

word= {
"a": ["10"],
"b": ["7"],
"c": ["-1"],
"d":["-1"],
"e": ["5","9"],
"f":["-1"],
"g":["-1"],
"h":["-1"],
"i":["-1"],
"j":["-1"],
"k":["11"],
"l":["-1"],
"m":["3","4"],
"n":["-1"],
"o":["-1"],
"p": ["-1"],
"q":["-1"],
"r": ["6","8"],
"s":["1"],
"t":["-1"],
"u":["2"],
"v":["-1"],
"w":["-1"],
"x":["-1"],
"y":["-1"],
"z":["-1"]
}
dash="___________"
count = 0
guess=input("guess a letter")
while count < 6:
    if guess[word] == ["-1"]:
               count = count+1
               hangman(count)
    else:
        for i in word[guess]:
               dash = dash[:i-1] + guess + dash[i:]
        print (dash)
    guess= input("guess a letter")



               





    
