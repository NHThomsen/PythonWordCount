class wordCounter():
    def wordCount(self, inputWords = ""):
        counts = dict()
        words = inputWords.split()
        
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        return counts