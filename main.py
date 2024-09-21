from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased", device=-1)
sentiment_result = classifier("I hate you")[0]
print(sentiment_result)

# text_generator = pipeline("text-generation", model="distilgpt2")
# text_result = text_generator(
#     "I hate you",
#     max_length=50,
#     num_return_sequences=5,
# )
# print(text_result)
