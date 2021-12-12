import wikipedia
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np


def get_wiki(query):
    title = wikipedia.search(query)[0]          # get the first article
    page = wikipedia.page(title)
    return page.content

# def get_comments(filename):
#     comments_file = open(filename, 'r')
#     return comments_file.read()


def create_word_cloud(text):
    mask = np.array(Image.open('cloud.png'))
    stopwords = set(STOPWORDS)
    wc = WordCloud(mask=mask, max_words=200, stopwords=stopwords, background_color='black')
    wc.generate(text)
    # wc.to_file('Comments Word Cloud.png')
    wc.to_file('Wiki Word Cloud.png')


# create_word_cloud(get_comments('comments.txt'))
create_word_cloud(get_wiki('python programming language'))
