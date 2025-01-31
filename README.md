# git-clone-https-github.com-smoken64-smoke-cpython.git-cd-smoke-cpython

## Running the Flask Application

To run the Flask application, follow these steps:

1. Navigate to the `multi-repo-endpoint` directory:
    ```bash
    cd multi-repo-endpoint
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

3. Run the Flask application:
    ```bash
    python app.py
    ```

## Using the `/api/repositories` Endpoint

To use the `/api/repositories` endpoint, send a POST request with a JSON payload containing a list of repository URLs. For example:

```json
{
    "repositories": [
        "https://github.com/user/repo1.git",
        "https://github.com/user/repo2.git"
    ]
}
```

The endpoint will clone each repository, perform analysis, and return the results in a JSON response.
