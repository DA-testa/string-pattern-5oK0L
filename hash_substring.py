# Vlads Sokolovs, 221RDB276

# python3

def hash(inputText):
    multiplier=7
    letters = [*inputText]
    sum=0
    for i in range(len(inputText)):
        sum=sum+ord(letters[i])*(multiplier**(len(inputText)-i))
    return sum


def read_input():
    firstInput = input()
    if firstInput[0]=="F":
        file=open(str("tests/06"), "r")
        pattern = file.readline()
        text = file.readline()
        return (pattern.rstrip(), text.rstrip())
    else:
        return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    matches = []
    for k in range(len(text)-len(pattern)+1):
        subText=text[k:k+len(pattern)]
        if hash(pattern) == hash(subText):
            if subText==pattern:
                matches.append(k)
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return matches


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
