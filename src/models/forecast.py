import pandas as pd
from datetime import datetime, timedelta
import requests
from io import StringIO

# Load your CSV data into a Pandas DataFrame
df = pd.read_csv('/Users/asmak/Documents/Sem 3/Adv ML/AT2/merged_data.csv')

# Define an API endpoint (you can change the URL as needed)
api_endpoint = 'https://github.com/asmitaskamble/AT2_ML-as-a-Service.git/sales/national/'

def get_sales_forecast(api_endpoint, input_date):
    try:
        # Convert the input date to a datetime object
        input_date = datetime.strptime(input_date, '%Y-%m-%d')

        # Calculate the date range for the next 7 days
        end_date = input_date + timedelta(days=7)

        # Filter the DataFrame for the date range
        filtered_data = df[(df['date'] >= input_date) & (df['date'] <= end_date)]

        # Calculate the sales forecast for the next 7 days
        forecast = filtered_data['sales'].sum()

        # Make a GET request to the API
        response = requests.get(f"{api_endpoint}{input_date}", params={"forecast": forecast})

        if response.status_code == 200:
            return response.json()
        else:
            return f"API request failed with status code {response.status_code}"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    # Accept user input for date
    input_date = input("Enter date (YYYY-MM-DD): ")
    result = get_sales_forecast(api_endpoint, input_date)
print(result)