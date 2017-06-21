import sys
import math
from pattern.en import parsetree
from word import *

## Concordance class creates an object with a dictionary and file name
class Concordance:
    def __init__(self, fileName):
        self.fileName = fileName
        self.concordance = dict()
        Concordance.add(self, fileName)

    def add(self, fileName):
        try:
            file = open(fileName, 'r')
            Concordance.parseFile(self, file)
            file.close()
        except IOError:
            raise ValueError("Could not open file")

    def isPunctuation(self, word):
        punctuation = set('.,?!:;')
        if any((p in punctuation) for p in str(word.type)):
            return True
        else:
            return False

    def checkWord(self, word):
        if not(Concordance.isPunctuation(self, word)):
            words = word.string.split('-')
            return words
        else:
            return []

    def addWord(self, word, sentence):
        if word in self.concordance:
            Word.add(self.concordance[word], sentence)
        else:
            self.concordance[word] = Word(sentence)

    def parseFile(self, file):
        text = file.read().replace('\n', ' ')
        tokenizedText = parsetree(text)
        sentenceId = 1
        for sentence in tokenizedText:
            for word in sentence:
                for w in Concordance.checkWord(self, word):
                    Concordance.addWord(self, w.lower(), sentenceId)
            sentenceId += 1

    def getFileName(self):
        return self.fileName

    def getWordCount(self):
        count = 0
        for key,value in self.concordance.items():
            count += Word.getWordCount(value)
        return count

    def getConcordance(self):
        return self.concordance

    ## Return a letter based on the number in the index
    ## Used for ordering the list
    def alphabetList(self, index):
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        multiplier = int(math.floor(index / 26) + 2)
        string = ""
        index = index % 26
        for x in range(1, multiplier):
            string += letters[index]
        return string + '.'

    def writeConcordance(self):
        string = ""
        index = 1
        for key, value in sorted(self.concordance.items()):
            line = ""
            # Uncomment to use letters instead of numbers
            # line += alphabetList(self, index) + " " + key
            line += str(index) + ". " + key
            whiteSpace = 30 - len(line)
            for x in range(1,whiteSpace):
                line += " "
            line += Word.writeWord(value) + "\n"
            string += line
            index += 1
        return string
