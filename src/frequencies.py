import os

from collections import Counter

def freqToFile(sortedFreq, totalLetters, filePath):
    if os.path.exists(os.path.join("src", "Files", "Frequencies", filePath)):
        mode = "w"
    else:
        mode = "x"
        
    with open(os.path.join("src", "Files", "Frequencies", filePath), mode) as freqFile:
        for letter, count in sortedFreq:
            if count > 5: # napise samo frekvence > 5
                percent = (count / totalLetters) * 100
                freqFile.write(f"{letter}: {count} ({percent:.2f}%)\n")

def calcLetterFrequencies(filePath):
    try:
        with open(os.path.join("Files", filePath), "rt") as file:
            content = file.read()

        # preskoci enter-je
        content = content.replace('\n', '')

        # presteje ponavljajocih crk OP
        letterFreq = Counter(content)
        totalLetters = len(content)

        # sortira padajoce, Counter v tuple
        sortedFreq = sorted(letterFreq.items(), key = lambda x : x[1], reverse = True)

        # za lazje branje
        freqToFile(sortedFreq, totalLetters, filePath="letterFrequencies.txt")

        for letter, count in sortedFreq:
            if letter.isalpha(): # samo crke
                percent = (count / totalLetters) * 100
                print(f"{letter}: {count} ({percent:.2f}%)")

    except FileNotFoundError:
        print(f"Error: File {filePath} not found. ")

def calcBigramFrequencies(filePath):
    try:
        with open(os.path.join("Files", filePath), "rt") as file:
            content = file.read()

        # preskoci enter-je
        content = content.replace('\n', '')

        bigrams = [content[i:i+2] for i in range(len(content)- 1)]

        # presteje ponavljajocih bigram OP
        bigramFreq = Counter(bigrams)
        totalLetters = len(bigrams)

        # sortira padajoce, Counter v tuple
        sortedFreq = sorted(bigramFreq.items(), key = lambda x : x[1], reverse = True)

        # za lazje branje
        freqToFile(sortedFreq, totalLetters, filePath="bigramFrequencies.txt")

        for letter, count in sortedFreq:
            if letter.isalpha(): # samo crke
                percent = (count / totalLetters) * 100
                print(f"{letter}: {count} ({percent:.2f}%)")

    except FileNotFoundError:
        print(f"Error: File {filePath} not found. ")


def calcTrigramFrequencies(filePath):
    try:
        with open(os.path.join("src", "Files", filePath), "rt") as file:
            content = file.read()

        # preskoci enter-je
        content = content.replace('\n', '')

        trigrams = [content[i:i+3] for i in range(len(content)- 1)]

        # presteje ponavljajocih bigram OP
        trigramFreq = Counter(trigrams)
        totalLetters = len(trigrams)

        # sortira padajoce, Counter v tuple
        sortedFreq = sorted(trigramFreq.items(), key = lambda x : x[1], reverse = True)

        # za lazje branje
        freqToFile(sortedFreq, totalLetters, filePath="trigramFrequencies.txt")

        for letter, count in sortedFreq:
            if letter.isalpha(): # samo crke
                percent = (count / totalLetters) * 100
                print(f"{letter}: {count} ({percent:.2f}%)")

    except FileNotFoundError:
        print(f"Error: File {filePath} not found. ")
