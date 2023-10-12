import requests

def get_github_repo_info(owner, repo_name):
    # Define the GitHub API URL for the repository
    url = f"https://api.github.com/repos/{owner}/{repo_name}"

    # Send an HTTP GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        repo_info = response.json()

        # Extract the information you need
        name = repo_info['name']
        description = repo_info['description']
        api_url = repo_info['url']
        input_parameters_url = repo_info["owner"]["login"]  # This is just an example

        # Print the information
        print(f"Repository Name: {name}")
        print(f"Description: {description}")
        print(f"API URL: {api_url}")
        print(f"Input Parameters URL: {input_parameters_url}")

    else:
        print(f"Failed to fetch repository information. Status code: {response.status_code}")

if __name__ == '__main__':
    owner = "asmitaskamble"
    repo_name = "AT2_ML-as-a-Service"
    get_github_repo_info(owner, repo_name)