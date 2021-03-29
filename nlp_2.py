from textblob import TextBlob
import nltk

# nltk.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())
"""
print(blob.word_counts["juliet"])

print(blob.word_counts["romeo"])

print(blob.word_counts["thou"])

print(blob.words.count("joy"))

print(blob.noun_phrases.count("lady capulet"))
"""
stops = stopwords.words("english")

more_stops = ["thee", "thy", "thou"]

stops += more_stops
# print(stops)

# Let's call the blob.word_counts dictionary's items method to get a list of word-frequency
items = blob.word_counts.items()
# type - dictionary items, prints every word with # of times they appear

# use a list comprehension to eliminate any tuples containing stop words:

items = [item for item in items if item[0] not in stops]

print(items[:10])

# TO Determine the top 20 words, let's sort the tuples in items in descending order by
# We can use built-in function sorted with a key argument to sort the tuples by the fre
# element in each tuple. To specify the tuple element to sort by, use the itemgetter function
# from the python standard libary's operator module:

from operator import itemgetter

sorted_items = sorted(items)
# prints based on alphabetical order

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
# prints based on number count

print(sorted_items[:10])


# grab the top 20
top20 = sorted_items[:20]
print(top20)

df = pd.DataFrame(top20, columns=["word", "count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(
    x="word", y="count", rot=0, legend=False, color=["y", "c", "m", "b", "g", "r"]
)

plt.gcf().tight_layout()

plt.show()

# WORDCLOUD -- Make sure to install wordcloud

from pathlib import Path
from wordcloud import WordCloud
import imageio

text = Path("RomeoAndJuliet.txt").read_text()
# print(text)

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

plt.imshow(wordcloud)
print("done")
