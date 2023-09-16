from sklearn.datasets import fetch_20newsgroups
import json

# Fetch the 20 newsgroups dataset
newsgroups = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))

# Get the list of newsgroup categories
categories = newsgroups.target_names

# Create an empty list to store intents
intents = {"intents": []}

# Iterate through the categories
for category_id, category_name in enumerate(categories):
    # Get posts from the current category
    posts = [text.strip() for text in newsgroups.data if newsgroups.target_names[newsgroups.target[list(newsgroups.data).index(text)]] == category_name]

    # Create an intent entry
    intent = {
        "tag": category_name.lower().replace(" ", "_"),
        "patterns": posts
    }

    # Append the intent to the list
    intents["intents"].append(intent)

# Save the intents to a JSON file
with open('intents.json', 'w') as file:
    json.dump(intents, file, indent=4)

print("intents.json file created successfully.")
