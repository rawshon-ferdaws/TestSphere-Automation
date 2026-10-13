import requests  # Import the library for sending HTTP requests

# Define the base URL for the REST API
BASE_URL = "https://jsonplaceholder.typicode.com"


# TC_API_001: Verify GET All Posts
def test_get_all_posts():

    # Send a GET request to retrieve all posts
    response = requests.get(
        f"{BASE_URL}/posts",
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify successful HTTP response (200 OK)
    assert response.status_code == 200

    # Convert the JSON response into Python data
    posts = response.json()

    # Verify the response data type is a list
    assert isinstance(posts, list)

    # Verify that at least one post is returned
    assert len(posts) > 0

    # Verify each post contains all required fields
    for post in posts:
        assert "id" in post
        assert "userId" in post
        assert "title" in post
        assert "body" in post


# TC_API_002: Verify GET Single Post
def test_get_single_post():

    # Define the ID of the post to retrieve
    post_id = 1

    # Send a GET request to retrieve a specific post
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify successful HTTP response (200 OK)
    assert response.status_code == 200

    # Convert the JSON response into Python data
    post = response.json()

    # Verify the response data type is a dictionary
    assert isinstance(post, dict)

    # Verify the returned post ID matches the requested ID
    assert post["id"] == post_id

    # Verify the response contains all required fields
    assert "userId" in post
    assert "title" in post
    assert "body" in post

    # Verify the title and body are not empty
    assert len(post["title"]) > 0
    assert len(post["body"]) > 0


# TC_API_003: Verify GET Invalid Post
def test_get_invalid_post():

    # Define a post ID that does not exist
    post_id = 999999

    # Send a GET request for the nonexistent post
    response = requests.get(
        f"{BASE_URL}/posts/{post_id}",
        timeout=10  # Limit the request wait time to 10 seconds
    )

    # Verify HTTP 404 (Not Found) for an invalid post ID
    assert response.status_code == 404

    # Convert the JSON response into Python data
    post = response.json()

    # Verify the response is an empty dictionary
    assert isinstance(post, dict)
    assert post == {}
