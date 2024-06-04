from src.frequencies import *
from src.decryption import *
# from openai import OpenAI

def main():
    encryptedFilePath = "encrypted.txt"
    decryptedFilePath = "decrypted.txt"

    if os.path.exists(os.path.join("Files", decryptedFilePath)):
        resetDecryptFile(decryptedFilePath)

    calcLetterFrequencies(encryptedFilePath)
    calcBigramFrequencies(encryptedFilePath)
    calcTrigramFrequencies(encryptedFilePath)

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
