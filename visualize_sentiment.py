df_reviews["sentiment"].value_counts().plot(kind="bar", color=["green", "gray", "red"])
plt.title("Customer Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.show()

# Sentiment Over Time
df_reviews["submission_time"] = pd.to_datetime(df_reviews["submission_time"])  # Convert date column
sentiment_over_time = df_reviews.groupby(df_reviews["submission_time"].dt.date)["sentiment"].value_counts().unstack()

sentiment_over_time.plot(kind="line", figsize=(10,5))
plt.title("Sentiment Over Time")
plt.xlabel("submission_time")
plt.ylabel("Count")
plt.legend(title="Sentiment")
plt.show()
