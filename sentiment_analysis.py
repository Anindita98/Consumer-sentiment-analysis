def get_sentiment(text):
    score = sia.polarity_scores(text)['compound']
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"
df_reviews["sentiment"] = df_reviews["review_text"].apply(get_sentiment)
print(df_reviews["sentiment"].value_counts())
