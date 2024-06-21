"""
This question is the reverse of the GFG question:
"Convert a sentence into its equivalent mobile numeric keypad sequence"


Given a mobile numeric keypad sequence from the old phones with button keypads (nokia, Motorolla, Sony Ericcson), 
convert it to its equivalent letter sequence

Consider the number to letter mapping

abc - 2
def - 3
ghi - 4
jkl - 5
mno - 6
pqrs - 7
tuv - 8
wxyz - 9

Assume all letters are in fully upper case or lowercase


used a two pointer approach,
start for the first, i for the end
let start be stationary until i comes across a different letter
at this point, extract the sequence, look up the hashmap and append it to the result
now move start to i + 1
repeat
at the end, one subsequence is left, extract it and get the letter from the hashmap
"""




def typeSentence(sentence) -> str:
    
    sequence = {
        '2':'a',
        '22':'b',
        '222':'c',
        '3': 'd',
        '33':'e',
        '333':'f',
        '4':'g',
        '44':'h',
        '444':'i',
        '5': 'j',
        '55': 'k',
        '555': 'l',
        '6': 'm',
        '66': 'n',
        '666': 'o', 
        '7': 'p',
        '77': 'q',
        '777': 'r',
        '7777': 's',
        '8': 't',
        '88': 'u',
        '888': 'v',
        '9':'w',
        '99': 'x',
        '999': 'y',
        '9999':'z' }
    if len(sentence) == 1:
        return sequence[sentence]
    res = ''
    start = 0
    for i in range(len(sentence) - 1):
        
        if sentence[start] != sentence[i + 1]:
            sub = sentence[start:i+1]
            res += sequence[sub]
            start = i + 1

    # the last sequence is unhandled
    # 4 4 4 5 5 5 6 6 6
    #             s   i
    # the above shown is the final values of start and i before exitting the loop
    res += sequence[sentence[start:i+2]]
    
    return res