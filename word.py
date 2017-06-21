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
