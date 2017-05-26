import sys
import math
from pattern.en import parsetree

## Return a letter based on the number in the index
## Used for ordering the list
def alphabetList(index):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    multiplier = int(math.floor(index / 26) + 2)
    string = ""
    index = index % 26
    for x in range(1, multiplier):
        string += letters[index]
    return string + '.'

## Word object has a list of sentences the word occurs in along with a word count
class Word:
    def __init__(self, sentence):
        self.sentences = [sentence]
        self.count = 1

    def add(self, sentence):
        self.sentences.append(sentence)
        self.count += 1

    def writeWord(self):
        sentences = str(self.sentences).strip('[]').replace(" ", "")
        return "{"+str(self.count)+":"+sentences+"}"

## Concordance class creates an object with a dictionary and file name
class Concordance:
    def __init__(self, fileName):
        self.fileName = fileName
        self.concordance = dict()

    def add(self, word, sentence):
        if word in self.concordance: # If word is in dictionary then add to the existing word object
            Word.add(self.concordance[word], sentence)
        else: # Create new word object otherwise
            self.concordance[word] = Word(sentence)

    def writeConcordance(self):
        string = self.fileName + ":"
        index = 0
        for key, value in sorted(self.concordance.items()):
            line = ""
            line += "\n"+ alphabetList(index) + " " + key
            whiteSpace = 28 - len(line)
            print whiteSpace
            for x in range(1,whiteSpace):
                line += " "
            line += Word.writeWord(value)
            string += line
            index += 1
        return string

## This function takes an open file and an concordance object
## Parses the text of the file using parsetree
def parseFile(file, concordance):
    text = file.read().replace('\n', ' ')
    tokenizedText = parsetree(text)
    for sentence in tokenizedText:
        for word in sentence:
            if word.type.isalpha(): # Makes sure word is a word and not a punctuation
                Concordance.add(concordance, word.string.lower(), word.sentence.id)
    print Concordance.writeConcordance(concordance)

## This function checks the parameters for a file name and opens the file
## Then calls parseFile on the opened file
def openFile():
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        file = open(fileName, 'r')
        try:
            concordance = Concordance(fileName)
            parseFile(file, concordance)
        finally:
            file.close()
    else:
        raise ValueError("File name parameter not passed")

if  __name__ =='__main__':openFile()
