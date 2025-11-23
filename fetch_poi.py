import requests

# Wikimedia API endpoint
base_url = "https://en.wikipedia.org/w/api.php"

# POI name to search
poi_name = input("Enter the name of the POI: ")  # Example: "Eiffel Tower"

# Define the parameters for the API request
params = {
    "action": "query",
    "format": "json",
    "titles": poi_name,  # Title of the Wikipedia page
    "prop": "extracts|info",
    "exintro": True,  # Get only the introduction section
    "explaintext": True,  # Get plain text
    "inprop": "url"  # Include the full URL of the page
}

# Send a GET request to the Wikimedia API
response = requests.get(base_url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    pages = data.get('query', {}).get('pages', {})
    
    # Extract information
    for page_id, page in pages.items():
        title = page.get('title', 'No Title')
        extract = page.get('extract', 'No Description Available')
        url = page.get('fullurl', 'No URL Available')
        
        print(f"\nTitle: {title}")
        print(f"Description: {extract}")
        print(f"Full URL: {url}")
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
