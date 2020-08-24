class wordCounter():
    wordsToRemoveSet = {}
    def wordCountDuringProcessing(self, textToCount = ""):
        if textToCount != "":
            counts = dict()
            words = textToCount.split()
        
            for word in words:
                if word not in self.wordsToRemoveSet:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
            return counts
        else:
            return ""
    def wordCountPostProcessing(self, textToCount = ""):
        if textToCount != "":
            counts = dict()
            words = textToCount.split()

            for word in words:
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
    def wordsToRemove(self, removeWords):
        self.wordsToRemoveSet = removeWords