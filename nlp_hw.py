from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
from pathlib import Path
import pandas as pd
from operator import itemgetter

blob = TextBlob(Path("book of John text.txt").read_text())

stops = stopwords.words("english")

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]

stops += more_stops

items = blob.word_counts.items()

items = [item for item in items if item[0] not in stops]

sorted_items = sorted(items)

sorted_items = sorted(items, key=itemgetter(1), reverse=True)

sorted_items = sorted_items[:16]

print(type(sorted_items))

sorted_itemslist = [item[0] for item in sorted_items]

print(sorted_itemslist)

sorted_itemslist = " ".join(sorted_itemslist)

import matplotlib.pyplot as plt
from pathlib import Path
from wordcloud import WordCloud
import imageio


# text = Path("book of John text.txt").read_text()


wordcloud = WordCloud(colormap="prism", background_color="white")

wordcloud = wordcloud.generate(sorted_itemslist)

wordcloud = wordcloud.to_file("BookOfJohn.png")

plt.imshow(wordcloud)
print("done")
