import wordCounter
import time

secondsBefore = time.time()

inputText = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas at purus augue. Nulla vel rutrum ante. Integer sed congue libero. Sed egestas urna nec semper interdum. Vestibulum vel nulla suscipit, blandit tortor non, pretium sem. Cras sed blandit enim, sodales auctor arcu. Pellentesque ac bibendum dolor. Integer sed nunc in quam scelerisque aliquam tempor at metus. Donec sit amet commodo mauris. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec libero tellus, finibus vel ipsum a, euismod vulputate nisl. Etiam aliquet a lacus pulvinar dapibus.
Aliquam erat volutpat. Cras dapibus id mi et egestas. Mauris ac diam sed tellus aliquet tristique. Aenean placerat purus velit, eget vulputate risus mattis ac. Mauris a suscipit sapien. Praesent tristique, neque et accumsan finibus, dui risus rutrum enim, nec condimentum risus nisl gravida orci. In sit amet aliquet nulla, sed mollis metus. Donec et dapibus est, eu finibus odio. Etiam non lacinia dolor, sit amet luctus ipsum. Nunc et facilisis quam. Nulla quis finibus elit. Vivamus a nisi a metus rutrum porttitor nec non odio. Nulla eget rutrum nibh.
Aenean rutrum scelerisque sagittis. Ut consectetur lacus ligula, at elementum tortor consequat dapibus. Sed ipsum nisi, posuere ac ex sed, laoreet aliquet velit. Curabitur condimentum ac eros in lobortis. Proin ultrices sit amet nulla in consectetur. Mauris facilisis nulla a nisi ultricies pellentesque. Proin at iaculis diam, eget interdum diam. Sed commodo sem laoreet magna placerat, at maximus leo vehicula. Donec eu enim faucibus, dapibus nulla nec, tempus enim. Nam imperdiet quam leo, vitae pharetra lorem dignissim et. Aliquam euismod risus eu mi ullamcorper, sit amet semper elit pulvinar. Maecenas quis ligula quis felis dapibus consequat quis eget quam. Nunc consequat posuere orci, sed venenatis nibh placerat eget. Quisque efficitur sem at sapien lacinia, ut blandit urna pharetra.
Suspendisse venenatis mi non magna varius, ac tincidunt mauris auctor. Pellentesque dapibus libero non dolor finibus porta. In imperdiet leo enim, ut rutrum magna rhoncus ut. Nullam mauris erat, ornare ut magna quis, interdum fringilla dui. Cras sollicitudin nibh a vulputate ultrices. Mauris tincidunt libero eu purus lacinia faucibus. Fusce nec tempor est. Nulla facilisi. Vivamus ac orci vitae tortor auctor tincidunt. In feugiat non nisi id euismod. Sed aliquet congue elit sit amet venenatis. Etiam rhoncus convallis lectus, ut feugiat tellus pharetra quis. Suspendisse accumsan malesuada odio, non congue nisi pharetra at. Quisque molestie diam nec sollicitudin laoreet. Donec eu turpis dignissim, porta lacus a, vulputate purus. Maecenas et purus aliquam, vulputate erat ac, laoreet nunc.
Integer ligula mauris, molestie at turpis ac, dapibus volutpat libero. Ut eu felis porta, imperdiet augue in, egestas metus. Nam egestas iaculis scelerisque. Phasellus in sem rutrum, tincidunt ipsum sit amet, dictum quam. Quisque tempor dolor quis gravida sagittis. Nulla laoreet egestas nisl, in euismod quam blandit et. Pellentesque in sapien eu augue consequat faucibus at tincidunt orci. Vivamus vel auctor mi, vitae condimentum ante. Mauris et neque volutpat, tristique elit sit amet, dapibus urna. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per."""
counter = wordCounter.wordCounter()
counter.wordsToRemove({"sit","amet","at","et","dapibus","eu","rutrum","sed","ac","in"})
counted = sorted(counter.wordCountPreProcessing(inputText).items(), key=lambda x: x[1], reverse=True)
#counted = sorted(counter.wordCountDuringProcessing(inputText).items(), key=lambda x: x[1], reverse=True)
#counted = sorted(counter.wordCountPostProcessing(inputText).items(), key=lambda x: x[1], reverse=True)

print(time.time() - secondsBefore)

#for i in counted:
    #print(i[0], i[1])