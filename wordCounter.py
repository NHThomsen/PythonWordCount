class wordCounter():
    wordsToRemoveSet = {}
    def wordsToRemove(self, removeWords):
        self.wordsToRemoveSet = removeWords
    # Removes words during counting
    def wordCountDuringProcessing(self, textToCount = ""):
        if textToCount != "":
            counts = dict()
        
            for word in textToCount.split():
                if word not in self.wordsToRemoveSet:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
            return counts
        else:
            return ""
    # Removes words post counting
    def wordCountPostProcessing(self, textToCount = ""):
        if textToCount != "":
            counts = dict()

            for word in textToCount.split():
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word]  = 1
            copiedCounts = dict(counts)
            for word in copiedCounts:
                if word in self.wordsToRemoveSet:
                    del counts[word]
            return counts
        else:
            return ""
    # Removes words pre counting
    def wordCountPreProcessing(self, textToCount = ""):
        if textToCount != "":
            counts = dict()

            for word in self.wordsToRemoveSet:
                textToCount = textToCount.replace(word,'')
            for word in textToCount.split():
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
            return counts
        else:
            return ""
            