import requests
import pandas as pd
import time
api_key = 'AIzaSyDiy0-4q4ERMHFeJu5EU5QK4yPIO2g5yDa'
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
# Read queries from the file
with open('/Users/macbookpro/Desktop/DISSERTATION/CODES/querryLONDON.txt', 'r') as file:
    queries = file.read().splitlines()
# Create a list to store all the restaurant data
all_restaurant_data = []
# Make API requests for each query
for query in queries:
    # Set parameters for the API request
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    params = {
        'key': api_key,
        'query': query
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        # Process the response data
        for result in data['results']:
            place_id = result['place_id']
            name = result['name']
            address = result['formatted_address']
            rating = result.get('rating', 'N/A')
            num_ratings = result.get('user_ratings_total', 'N/A')

            # Retrieve place details to get reviews
            details_url = 'https://maps.googleapis.com/maps/api/place/details/json'
            details_params = {
                'key': api_key,
                'place_id': place_id,
                'fields': 'reviews'
            }
            try:
                details_response = requests.get(details_url, params=details_params)
                details_data = details_response.json()
                # Process the review data
                if 'result' in details_data and 'reviews' in details_data['result']:
                    reviews_data = details_data['result']['reviews']
                    for review in reviews_data:
                        author_name = review.get('author_name', 'N/A')
                        review_rating = review.get('rating', 'N/A')
                        text = review.get('text', 'N/A')
                        review_location = review.get('relative_time_description', 'N/A')
                        # Append review information to the list
                        review_info = {'Query': query, 'Restaurant': name, 'Address': address, 'Rating': rating,
                                       'Num Ratings': num_ratings, 'User': author_name, 'Review Rating': review_rating,
                                       'Review': text, 'Location': review_location}
                        all_restaurant_data.append(review_info)
            except requests.exceptions.RequestException as e:
                print(f"Error in details request for '{query}': {e}")
    except requests.exceptions.RequestException as e:
        print(f"Error in search request for '{query}': {e}")
    # Add a delay to avoid exceeding the API quota
    time.sleep(2)
# Create a pandas DataFrame from the all_restaurant_data list
df = pd.DataFrame(all_restaurant_data)
# Save the DataFrame to an Excel file
filename = '/Users/macbookpro/Desktop/DISSERTATION/DATA/LONDON_test.xlsx'
df.to_excel(filename, index=False)
print(f"Data saved as '{filename}'")







