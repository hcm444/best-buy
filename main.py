import requests
import json

# Your Best Buy API key
api_key = "YOUR_API_KEY"

# The zip code to search around
zip_code = "10001"

# The radius to search within (in miles)
radius = "25"

# The SKU to search for
sku = "12345"

# Construct the API request URL
url = "https://api.bestbuy.com/v1/stores(area({},{}))+products(sku={})?apiKey={}&format=json".format(zip_code, radius,
                                                                                                     sku, api_key)

try:
    # Send the API request
    response = requests.get(url)

    # Check if the request was successful
    response.raise_for_status()

    # Parse the response as JSON
    data = json.loads(response.text)

    if data["total"] > 0:
        for store in data["stores"]:
            print("Store Name: ", store["name"])
            print("Store Address: ", store["address"])
            print("Store City: ", store["city"])
            print("Store Distance: ", store["distance"])
            print("Store Phone: ", store["phone"])
    else:
        print("No stores found.")

except requests.exceptions.HTTPError as err:
    print("HTTP Error Occured : ", err)
except requests.exceptions.RequestException as e:
    # handle other errors
    print("Request Error Occured : ", e)
