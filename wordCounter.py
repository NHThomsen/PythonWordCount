class wordCounter():
    wordsToRemoveSet = {}
    def wordCount(self, textToCount = ""):
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
    def wordsToRemove(self, removeWords):
        self.wordsToRemoveSet = removeWords