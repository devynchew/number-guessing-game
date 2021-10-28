max = int(input("Enter the range: ")) # Get max number
johnsNumber = int(input(f'Think of a random number between 1 and {max} and press enter once done: ')) # Get the number the program has to guess
numberHasBeenGuessed = False
noOfQuestions = 0
candidates = list(range(1,max+1))
# breakpoint = 1 # Initialize first oldbreakpoint
i = 0
while not numberHasBeenGuessed:

    breakpointIndex = int(len(candidates)/2)
    oldbreakpoint = breakpoint
    breakpoint = candidates[breakpointIndex]
    userinput = input(f'Is it smaller than {breakpoint}, \'y\' or \'n\'? ').lower()
    if userinput == 'y':
        if i == 0:
            oldbreakpoint = 1
        elif breakpoint < oldbreakpoint:
            oldbreakpoint = candidates[0]
        candidates = list(range(oldbreakpoint,breakpoint))
    else:
        if i == 0:
            oldbreakpoint = max + 1
        elif oldbreakpoint < breakpoint:
            oldbreakpoint = candidates[-1] + 1
        candidates = list(range(breakpoint,oldbreakpoint))
    noOfQuestions += 1
    if len(candidates) == 1: # number has been guessed when only one number is left in the list
        numberHasBeenGuessed = True
    i += 1

print(f'Wonderful it took me {noOfQuestions} questions to find out that you had the number {candidates[0]} in mind!')