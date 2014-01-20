import sys
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
foundLetters = []
with open('commentFromOcrHtml.txt') as f:
        for line in f:
                for letter in alphabet:
                        if letter in line:
                                index = line.index(letter)
                                foundLetters.append(line[index])
sys.stdout.write(''.join(foundLetters))
sys.stdout.flush()
