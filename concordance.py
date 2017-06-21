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
        if not(sentence in self.sentences):
            self.sentences.append(sentence)
        self.count += 1

    def getWordCount(self):
        return self.count

    def getSentences(self):
        return self.sentences

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

    def getWordCount(self):
        count = 0
        for key,value in self.concordance.items():
            count += Word.getWordCount(value)
        return count

    def writeConcordance(self):
        string = ""
        index = 0
        for key, value in sorted(self.concordance.items()):
            line = ""
            line += alphabetList(index) + " " + key
            whiteSpace = 29 - len(line)
            for x in range(1,whiteSpace):
                line += " "
            line += Word.writeWord(value) + "\n"
            string += line
            index += 1
        return string

def isPunctuation(word):
    punctuation = set('.,?!:;')
    if any((p in punctuation) for p in str(word.type)):
        return True
    else:
        return False

def checkWord(word):
    if not(isPunctuation(word)):
        words = word.string.split('-')
        return words
    else:
        return []

## This function takes an open file and an concordance object
## Parses the text of the file using parsetree
def parseFile(file, concordance):
    text = file.read().replace('\n', ' ')
    tokenizedText = parsetree(text)
    for sentence in tokenizedText:
        for word in sentence:
            sentenceId = word.sentence.id
            for w in checkWord(word):
                Concordance.add(concordance, w.lower(), sentenceId)
    return concordance

## This function opens a given file and returns a Concordance Object
## Then calls parseFile on the opened file
def openFile(fileName):
    try:
        file = open(fileName, 'r')
        concordance = Concordance(fileName)
        output = parseFile(file, concordance)
        file.close()
        return output
    except IOError:
        print "File Opening Error"


if  __name__ =='__main__':
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
        openFile(fileName)
    else:
        raise ValueError("File name parameter not passed")
