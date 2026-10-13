import requests  # Import the library for sending HTTP requests

# Define the base URL for the REST API
BASE_URL = "https://jsonplaceholder.typicode.com"


# TC_API_004: Verify POST Valid Data
def test_create_post():

    # Define valid JSON data for creating a new post
    payload = {
        "title": "TestSphere API Automation",
        "body": "Testing POST request using Python Requests",
        "userId": 1
    }

    # Send a POST request with JSON data to create a post
    response = requests.post(
        f"{BASE_URL}/posts",
        json=payload,  # Automatically serialize data into JSON
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify successful resource creation (201 Created)
    assert response.status_code == 201

    # Convert the JSON response into Python data
    post = response.json()

    # Verify the response data type is a dictionary
    assert isinstance(post, dict)

    # Verify the response contains a generated post ID
    assert "id" in post
    assert isinstance(post["id"], int)

    # Verify the returned title matches the submitted title
    assert post["title"] == payload["title"]

    # Verify the returned body matches the submitted body
    assert post["body"] == payload["body"]

    # Verify the returned user ID matches the submitted user ID
    assert post["userId"] == payload["userId"]
