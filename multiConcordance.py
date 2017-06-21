import os
from concordance import *

# MultipleConcordance class
# Fields
#   - concordances
#       * Is a dictionary. The key is the fileName and the value is a Concordance object
#   - allConcordances
#       * Is a dictionary. The key is a unique word and the value is a list of all the
#       * files the word appears in
class MultipleConcordance:
    def __init__(self):
        self.concordances = dict()
        self.allConcordances = dict()

    # Add a file to the object
    def add(self, file):
        if os.path.isfile(file):
            concordance = openFile(file)
            MultipleConcordance.addConcordance(self, concordance) # Adds to the concordance object
            MultipleConcordance.addAllConcordances(self, concordance) # Adds to the allConcordances object
        else:
            raise ValueError("Input not a file")

    def addAllConcordances(self, concordance):
        # Get the dictionary and name fields from Concordance Object
        concordanceDictionary = Concordance.getConcordance(concordance)
        concordanceName = Concordance.getFileName(concordance)
        for key, value in concordanceDictionary.items():
            # Adds unique words to allConcordances field
            if key in self.allConcordances:
                self.allConcordances[key].append(concordanceName)
            else:
                self.allConcordances[key] = [concordanceName]

    def addConcordance(self, concordance):
        # Adds the concordance name and object key,value pair to self.concordances
        concordanceName = Concordance.getFileName(concordance)
        if not(concordanceName in self.concordances):
            self.concordances[concordanceName] = concordance

    # Returns a string with the specified concordance formatted.
    def writeConcordance(self, concordance):
        return Concordance.writeConcordance(concordance)

    # Returns a string with the all the concordances formatted.
    def writeAllConcordances(self):
        counter = 1
        string = ""
        for key, value in self.allConcordances.items():
            body = ""
            body += str(counter) + '. ' + key + '\n'
            for v in value:
                line = ""
                line += "     " + v
                concordance = self.concordances[v]
                concordanceDict = Concordance.getConcordance(concordance)
                word = concordanceDict[key]
                wordSentences = Word.getSentences(word)
                wordCount = Word.getWordCount(word)
                sentences = str(wordSentences).strip('[]').replace(" ", "")
                whiteSpace = 30 - len(line)
                for x in range(1,whiteSpace):
                    line += " "
                line += "{"+str(wordCount)+":"+sentences+"}"
                line += "\n"
                body += line
            counter += 1
            string += body
        return string


# Parameter can be either 1 directory or multiple files
if  __name__ =='__main__':
    if len(sys.argv) > 1: # Checks thats a parameter exists
        multiConcordance = MultipleConcordance() # Creates MultipleConcordance Object
        parameter = sys.argv[1]
        if (os.path.isdir(parameter)): # If checking directory for files
            path = os.path.dirname(os.path.realpath(__file__))
            os.chdir(path+"/"+parameter)
            path = os.path.dirname(os.path.realpath(__file__))
            for file in os.listdir(path):
                MultipleConcordance.add(multiConcordance, file)
            print MultipleConcordance.writeAllConcordances(multiConcordance)
        else: # Multiple file parameters
            for index in range(1,len(sys.argv)):
                file = sys.argv[index]
                MultipleConcordance.add(multiConcordance, file)
            print MultipleConcordance.writeAllConcordances(multiConcordance)
    else:
        raise ValueError("File name parameter not passed")
