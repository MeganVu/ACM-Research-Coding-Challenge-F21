import os
from textblob import TextBlob

def getPolarity(text):
  return TextBlob(text).sentiment.polarity

reader = open("input.txt")
file = reader.read()
final = getPolarity(file)
print(final)

