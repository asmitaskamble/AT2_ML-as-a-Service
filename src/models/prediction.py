import pandas as pd
import requests

# Load the CSV data into a DataFrame
sales_data = pd.read_csv('merged_data.csv')

# Define the API endpoint URL
api_url = 'https://github.com/asmitaskamble/AT2_ML-as-a-Service.git/sales/stores/items/'

# Function to get sales predictions
def get_sales_prediction(date, item, store):
    # Filter the data based on input parameters
    filtered_data = sales_data[(sales_data['date'] == date) & (sales_data['item'] == item) & (sales_data['store'] == store)]
    
    # Calculate the predicted sales volume
    if not filtered_data.empty:
        predicted_sales = filtered_data['sales'].mean()
        return predicted_sales
    else:
        return "No data found for the given input."

# Accept user input for date, item, and store
date = input("Enter date (YYYY-MM-DD): ")
item = input("Enter item: ")
store = input("Enter store: ")

# Make the API request and get the response
response = requests.get(f'{api_url}?date={date}&item={item}&store={store}')

if response.status_code == 200:
    predicted_sales = response.json()['predicted_sales']
    print(f"Predicted Sales for {date}, {item}, {store}: {predicted_sales}")
else:
    print("Error: Unable to fetch data from the API.")
