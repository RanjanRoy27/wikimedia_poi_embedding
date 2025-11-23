POI Metadata Extraction & Keyword Detection

This project fetches Point of Interest (POI) information from Wikipedia using the Wikimedia API and extracts the most relevant keywords from the POI description using TF-IDF.

---

 Features

- Fetches POI description from Wikipedia
- Preprocesses text (tokenization, stopword removal)
- Extracts the most relevant words using TF-IDF
- Beginner-friendly Python scripts
- Useful for AI recommender systems and NLP projects

---
Project Files

fetch_poi.py # Fetches POI title, description, and URL from Wikipedia
fetch_poi_word.py # Fetches POI + extracts relevant keywords using TF-IDF
poi_processing.py # Contains NLTK data downloader
README.md # Project documentation



---

Installation

Install required Python libraries:
pip install requests
pip install nltk
pip install scikit-learn

Download NLTK data:
import nltk
nltk.download('punkt')
nltk.download('stopwords')

Usage
1. Fetch POI Description
python fetch_poi.py
2. Extract Relevant Words Using TF-IDF

python fetch_poi_word.py
Enter a POI name when asked (Example: Eiffel Tower).
Example Output

Enter the name of the POI: Eiffel Tower

Most Relevant Words:
['tower', 'eiffel', 'iron', 'paris', 'landmark']
Perfect For
Final year projects

Travel recommendation systems

NLP preprocessing

Wikipedia data extraction

Machine learning pipelines

Contributions
You can improve this project by adding:

BERT embeddings

Sentence Transformers

API version of the system

Keyword clustering

📜 License
This project is open-source under the MIT License.



---

# 🟢 **STEP 3 — Save the README.md file**
Once you paste the text → click “Save”.

---

# 🟢 **STEP 4 — Upload README.md to GitHub**
If you're using GitHub Website Upload:

1. Open your GitHub repository  
2. Click **Add File → Upload files**  
3. Upload `README.md`  
4. Click **Commit Changes**



