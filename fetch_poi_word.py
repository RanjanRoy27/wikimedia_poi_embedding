import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import nltk

# Download NLTK resources (only required once)
#nltk.download('punkt')
#nltk.download('stopwords')

# Define the function
def get_relevant_words(poi_name, top_n=20):
    """
    Fetch POI data from Wikimedia API and extract the most relevant words using TF-IDF.
    
    Args:
        poi_name (str): Name of the Point of Interest (POI) to search on Wikipedia.
        top_n (int): Number of most relevant words to return.
    
    Returns:
        list: Top `n` relevant words.
    """
    try:
        # Step 1: Fetch POI description using Wikimedia API
        base_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "format": "json",
            "titles": poi_name,
            "prop": "extracts",
            "exintro": True,
            "explaintext": True,
        }
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            return f"Error: Unable to fetch data (HTTP {response.status_code})"
        
        data = response.json()
        pages = data.get('query', {}).get('pages', {})
        
        # Extract the description
        description = ""
        for page_id, page in pages.items():
            description = page.get('extract', "")
            if not description:
                return f"No description found for POI: {poi_name}"
        
        # Step 2: Preprocess the text
        stop_words = set(stopwords.words('english'))
        tokens = word_tokenize(description.lower())
        tokens = [word for word in tokens if word.isalnum()]  # Remove punctuation
        tokens = [word for word in tokens if word not in stop_words]  # Remove stopwords
        processed_text = " ".join(tokens)
        
        # Step 3: Apply TF-IDF to extract relevant words
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([processed_text])
        scores = zip(vectorizer.get_feature_names_out(), tfidf_matrix.toarray()[0])
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        
        # Step 4: Return the top relevant words
        return [word for word, score in sorted_scores[:top_n]]
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
poi_name = input("Enter the name of the POI: ")
relevant_words = get_relevant_words(poi_name)
print(f"\nMost Relevant Words for '{poi_name}': {relevant_words}")
