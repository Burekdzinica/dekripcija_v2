import os

from collections import Counter
from openai import OpenAI

def freqToFile(sortedFreq, totalLetters):
    if os.path.exists(os.path.join("Files", "letterFrequencies.txt")):
        mode = "w"
    else:
        mode = "x"
        
    with open(os.path.join("Files", "letterFrequencies.txt"), mode) as freqFile:
        for letter, count in sortedFreq:
            percent = (count / totalLetters) * 100
            freqFile.write(f"{letter}: {count} ({percent:.2f}%)\n")

def calcFrequencies(filePath):
    try:
        with open(os.path.join("Files", filePath), "rt") as file:
            content = file.read()

        # preskoci enter-je
        content = content.replace('\n', '')

        # presteje ponavljajocih crk OP
        letterFreq = Counter(content)
        totalLetters = len(content) # je to res ???

        # sortira padajoce, Counter v tuple
        sortedFreq = sorted(letterFreq.items(), key = lambda x : x[1], reverse = True)

        # za lazje branje
        freqToFile(sortedFreq, totalLetters)

        for letter, count in sortedFreq:
            if letter.isalpha(): # samo crke
                percent = (count / totalLetters) * 100
                print(f"{letter}: {count} ({percent:.2f}%)")

    except FileNotFoundError:
        print(f"Error: File {filePath} not found. ")

def getEncryptedText(filePath):
    with open(os.path.join("Files", filePath), "r") as file:
        return file.read()
    
def getDecryptedText(filePath):
    with open(os.path.join("Files", filePath), "r") as file:
        return file.read()
    
def printDecryptedText(filePath):
    decryptedMsg = getDecryptedText(filePath)
    print(f"\nDecrypted message: \n\n{decryptedMsg}\n")

def resetDecryptFile(filePath):
    os.remove(os.path.join("Files", filePath))

def decrypt(filePath, decryptionMapping, msg):
    decryptedMsg = ''.join(decryptionMapping.get(char, char) for char in msg)

    if os.path.exists(os.path.join("Files", filePath)):
        mode = "w"
    else:
        mode = "x"
        
    with open(os.path.join("Files", filePath), mode) as file:
        file.write(decryptedMsg)

# Doda koncna locila
def addEndPuncutuation(text):
    if not text.endswith((".", "!", "?")):
        text += "."
    return text

# Uporab OpenAI za presledke, locila, ker brez ne bi znal. Sam rabim API key :(
def punctuation(filePath):
    apiKey = "sk-proj-CAlCQpiYzoU1HwWRAbrrT3BlbkFJ7FCsO2aqxkOL3fnW2XqM"
    client = OpenAI(api_key=apiKey)

    with open(os.path.join("Files", filePath)) as file:
        content = file.read()

    # zahteva AI
    chatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,  # content iz decrypted.txt
            }
        ],
        model="gpt-3.5-turbo",
    )

    # AI besedilo
    completedText = chatCompletion["choices"][0]["message"]["content"]

    textWithPunctuation = addEndPuncutuation(completedText)
    
    print(textWithPunctuation)

    if os.path.exists(os.path.join("Files", filePath)):
        mode = "w"
    else:
        mode = "x"
        
    with open(os.path.join("Files", filePath), mode) as file:
        file.write(textWithPunctuation)
    

def main():
    encryptedFilePath = "encrypted.txt"
    decryptedFilePath = "decrypted.txt"

    # resetDecryptFile(decryptedFilePath)

    calcFrequencies(encryptedFilePath)

    encryptedMsg  = getEncryptedText(encryptedFilePath)
    print (f"\nEncrypted message: \n\n{encryptedMsg}\n")

    decryptionMapping = {}

    while True:
        userInput = input("\nEnter letter to change, (e.g. X->e) or type \"exit\" to quit: ").strip()

        # exit
        if userInput.lower() == "exit":
            print("\nExiting program.")
            break

        # mapping decrypted letters
        try:
            changePair = userInput.split("->")
            encryptedLetter, decryptedLetter = changePair[0].strip(), changePair[1].strip() # [0] = X [1] = e 
            decryptionMapping[encryptedLetter] = decryptedLetter
            
        except (ValueError, IndexError):
            print("Invalid input. Please provide a valid letter change.")

        decrypt(decryptedFilePath, decryptionMapping, encryptedMsg)
        printDecryptedText(decryptedFilePath)

    # nimam API key-a
    # punctuation(decryptedFilePath)

if __name__ == "__main__":
    main()
