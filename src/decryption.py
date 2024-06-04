import os

# from openai import OpenAI

def saveFile(filePath, msg):   
    if os.path.exists(os.path.join("src", "Files", filePath)):
        mode = "w"
    else:
        mode = "x"
        
    with open(os.path.join("src", "Files", filePath), mode) as file:
        file.write(msg) 

def getEncryptedText(filePath):
    with open(os.path.join("src", "Files", filePath), "r") as file:
        return file.read()
     
def printDecryptedText(filePath):
    with open(os.path.join("src", "Files", filePath), "r") as file:
        decryptedMsg =  file.read()
    print(f"\nDecrypted message: \n\n{decryptedMsg}\n")

def resetDecryptFile(filePath):
    os.remove(os.path.join("src", "Files", filePath))

def decrypt(filePath, decryptionMapping, msg):
    decryptedMsg = ''.join(decryptionMapping.get(char, char) for char in msg)
    saveFile(filePath, decryptedMsg)

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

    saveFile(filePath, textWithPunctuation)
    