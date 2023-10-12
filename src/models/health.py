import requests

# Define the base URL where your server is running
base_url = "https://github.com/asmitaskamble/AT2_ML-as-a-Service.git"

# Define the endpoint you want to request
endpoint = "/health/"

# Send a GET request to the '/health/' endpoint
response = requests.get(base_url + endpoint)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Print the welcome message from the response
    print("Status Code: 200 OK")
    print("Welcome Message: " + response.text)
else:
    print(f"Request failed with status code: {response.status_code}")