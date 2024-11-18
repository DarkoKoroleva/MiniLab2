# Application

## Run

To run the collection web service execute command below in root of repo:

```shell
poetry run start-service
```

## Exit

Use keyboard interrupt

## API Documentation

This service provides three main functionalities using GitHub API: getting user subscribers, creating an Issue in a repository, and closing an Issue by its number. Below are the routes and their descriptions.

## 1. Getting User Subscribers
- **Route**: `/{username}`
- **Method**: `GET`
- **Logic**:
  - Creating a URL for a request to the GitHub API: `https://api.github.com/users/{username}/followers`.
  - Executing a `GET` request.
  - If the request is successful (**code 200**), the list of subscribers is returned in JSON format.
  - If the request is unsuccessful, an error message with a status code is returned.

## 2. Creating an Issue in the Repository
- **Route**: `/{owner}/{repo}`
- **Method**: `POST`
- **Logic**:
  - Creating a URL for creating an Issue in the repository: `https://api.github.com/repos/{owner}/{repo}/issues`.
  - Forming the request body with the `title` and `body` fields.
  - Executing a `POST` request.
  - If the request is successful (**code 201**), data about the created Issue is returned.
  - If the request is unsuccessful, an error message with a status code is returned.

## 3. Closing the Issue by Number
- **Route**: `/{owner}/{repo}/{issue_number}`
- **Method**: `PATCH`
- **Logic**:
  - Creating a URL to update the status of the task: `https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}`.
  - Sending a request with updated data by setting `"state": "closed"`.
  - Executing a `PATCH` request.
  - If the request is successful (**code 200**), updated Issue data is returned.
  - If the request is unsuccessful, an error message with a status code is returned.

## How to Use
To interact with the API, you can use tools like **Postman**, **cURL**, or a web browser (for `GET` requests). Below are some examples:

### Example of Getting User Subscribers
```bash
GET http://0.0.0.0:8000/{username}
```
## Link to the workspace

https://www.postman.com/daarrko/github-api-service/request/7uwu60o/close-issue?action=share&creator=39784122&ctx=documentation
