file_paths = [
    "reviews_250-500_masked.csv.zip",
    "reviews_500-750_masked.csv.zip",
    "reviews_0-250_masked.csv (1).zip",
    "reviews_750-1250_masked.csv.zip",
    "reviews_1250-end_masked.csv.zip"
]
df_list = [pd.read_csv(file) for file in file_paths]  
df_reviews = pd.concat(df_list, ignore_index=True)  
num_cols = df_reviews.select_dtypes(include=['number']).columns  
cat_cols = df_reviews.select_dtypes(include=['object']).columns  

df_reviews[num_cols] = df_reviews[num_cols].fillna(0)
df_reviews[cat_cols] = df_reviews[cat_cols].fillna("Unknown")

print(df_reviews.isnull().sum())
