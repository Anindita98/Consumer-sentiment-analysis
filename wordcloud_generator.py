positive_text = " ".join(df_reviews[df_reviews["sentiment"] == "Positive"]["review_text"])
negative_text = " ".join(df_reviews[df_reviews["sentiment"] == "Negative"]["review_text"])

plt.figure(figsize=(12,6))

# Positive Reviews
plt.subplot(1,2,1)
plt.title("Positive Word Cloud")
plt.imshow(WordCloud(background_color="white", colormap="Greens").generate(positive_text))
plt.axis("off")

# Negative Reviews
plt.subplot(1,2,2)
plt.title("Negative Word Cloud")
plt.imshow(WordCloud(background_color="white", colormap="Reds").generate(negative_text))
plt.axis("off")

plt.show()
