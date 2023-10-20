#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st

import numpy as np
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

st.title('Hotel Review Classifier')

review  = st.text_input("Enter some text", "")

# Create a VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment based on polarity score and defined scale
def classify_sentiment(polarity_score):
    if polarity_score >= 0.05:  # Positive
        return "positive"
    elif polarity_score <= -0.05:  # Negative
        return "negative"
    else:  # Neutral
        return "neutral"

# List of reviews
reviews = [ "I love this hotel! It's fantastic."]


sentiment_scores = analyzer.polarity_scores(review)
classified_sentiment = classify_sentiment(sentiment_scores['compound'])

st.write(f"\n Review is : {classified_sentiment}")


