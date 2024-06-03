import os
from collections import Counter

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
    
# def decrypt(filePath, decryptionMapping, msg):
#     decrypted_message = ''.join(decryptionMapping.get(char, char) for char in msg)

#     if os.path.exists(os.path.join("Files", filePath)):
#         mode = "w"
#     else:
#         mode = "x"
        
#     with open(os.path.join("Files", filePath), mode) as file:
#         file.write(decrypted_message)
    

def main():
    encryptedFilePath = "encrypted.txt"
    decryptedFilePath = "decrypted.txt"

    calcFrequencies(encryptedFilePath)

    encryptedMsg  = getEncryptedText(encryptedFilePath)
    print (f"\nEncrypted message: \n\n{encryptedMsg}\n")

    # decryptionMapping = {}

    while True:
        userInput = input("\nEnter letter to change, (e.g. X->e) or type \"exit\" to quit: ").strip()

        if userInput.lower() == "exit":
            print("\nExiting program.")
            break

        # decrypt(decryptedFilePath, decryptionMapping, encryptedMsg)


        decryptedMsg = getDecryptedText(decryptedFilePath)
        print(f"\nDecrypted message: \n\n{decryptedMsg}\n")

if __name__ == "__main__":
    main()
