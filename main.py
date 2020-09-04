import wordCounter
import time

secondsBefore = time.time()

inputText = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc lacinia lacus odio, sed sodales nibh euismod sed. In vulputate massa quis risus porttitor, at mattis magna ornare. Vivamus vel lectus et lectus efficitur ullamcorper. Suspendisse tristique orci lacus, sit amet laoreet lorem consequat vitae. Maecenas sed justo scelerisque ipsum sodales egestas non vel est. Proin placerat, dolor a auctor scelerisque, diam ante auctor ante, ut vehicula purus leo eget nunc. Maecenas imperdiet augue faucibus dolor scelerisque, in efficitur turpis dictum. In tortor nisi, auctor vitae egestas eget, finibus at nisi. Integer placerat, mauris eu auctor ornare, magna magna pulvinar diam, id varius lectus libero quis dolor. Proin mollis sapien laoreet, efficitur nisi nec, efficitur dui. Ut ornare auctor nunc, vel rhoncus libero vestibulum eget. Nulla luctus orci sed bibendum fringilla. Phasellus tempor tortor ex, a interdum lectus molestie a.
Phasellus finibus mauris vel commodo bibendum. Aliquam lacinia finibus turpis, sit amet interdum mauris. Aliquam blandit mi ipsum, suscipit cursus nisl tincidunt eu. Donec tincidunt, arcu ut commodo fringilla, metus lectus luctus orci, eget pretium dui libero at ex. Duis congue, orci sit amet pharetra sagittis, orci nulla gravida dolor, quis commodo nunc orci venenatis justo. Pellentesque non est a sem imperdiet dignissim. Integer ut laoreet elit. Vivamus mollis finibus velit pharetra eleifend. Sed sit amet felis varius, ornare odio ac, varius nibh. Pellentesque fermentum lobortis nunc, eget molestie felis fringilla a. Ut lacinia tortor ligula, sit amet interdum quam volutpat eget. Ut ante eros, gravida at lacinia a, molestie sed elit. Donec aliquet tempus ligula non venenatis. Phasellus suscipit pretium suscipit. Pellentesque maximus, dui a bibendum malesuada, quam massa porttitor neque, vel eleifend magna mi sit amet nisl.
Proin in sapien sit amet nunc condimentum rhoncus. Phasellus mattis ac neque ut rhoncus. In cursus ac tortor id posuere. Donec pellentesque quam augue, eu vestibulum sapien tincidunt vel. Nulla eros odio, iaculis consectetur arcu quis, rutrum vulputate nunc. Cras posuere efficitur malesuada. Duis eu justo id magna mollis efficitur. Cras a ante et nibh vestibulum fermentum ut ut nibh. Duis et urna dolor. Mauris elit felis, commodo at venenatis et, porta eu nulla. Integer placerat enim id maximus aliquet. Praesent ut ante non odio sagittis pharetra et eget ligula. Quisque consequat pretium magna, eget varius sapien tristique ut. Vivamus malesuada libero non rutrum ornare.
Pellentesque vel accumsan nisi, commodo sodales nisl. Suspendisse blandit nibh sit amet ipsum tincidunt facilisis. Sed tempor sagittis orci, at auctor erat accumsan id. Donec hendrerit, leo sit amet placerat venenatis, est lorem ultricies tellus, a porttitor lectus dui eu dui. Praesent vulputate, orci nec ullamcorper venenatis, arcu enim sagittis tortor, mollis tempus dolor mi non libero. Suspendisse potenti. Suspendisse potenti. Pellentesque a dignissim diam. Pellentesque auctor nibh leo, sit amet sagittis magna varius vel. Maecenas a sodales tellus. Curabitur convallis leo ac massa pretium, non porta purus condimentum.
In hac habitasse platea dictumst. Morbi feugiat pulvinar mi sed varius. Donec ut magna sapien. Ut tincidunt gravida lacus, vitae blandit elit consequat sit amet. Aenean lacinia pellentesque."""
counter = wordCounter.wordCounter()
counter.wordsToRemove({"sit","amet"})
counted = sorted(counter.wordCountPreProcessing(inputText).items(), key=lambda x: x[1], reverse=True)
#counted = sorted(counter.wordCountDuringProcessing(inputText).items(), key=lambda x: x[1], reverse=True)
#counted = sorted(counter.wordCountPostProcessing(inputText).items(), key=lambda x: x[1], reverse=True)

print(time.time() - secondsBefore)

#for i in counted:
    #print(i[0], i[1])