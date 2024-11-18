import requests
import uvicorn

from server import collection_host, collection_port, mini_app
from server.Human import Human
from server.IssueData import IssueData
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("GITHUB_TOKEN")

friends: list[Human] = []

@mini_app.get("/")
async def root():
    return friends

@mini_app.get('/{name}')
def get_followers(name: str):
    headers = {
        "authorization": f"token {token}"
    } if token else {}

    url = f"https://api.github.com/users/{name}/followers"

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        result = response.json()
        for user in result:
            friends.append(Human(user['login'], user['id']))
        print('OK')
        return friends
    elif response.status_code == 404:
        return {"status": 401,
                "message": "Ай-ай-ай, неверный токен авторизации!"}
    else:
        return response.json()


@mini_app.post('/{owner}/{repo}')
def create_github_issue(owner, repo, issue_data: IssueData):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.post(url, json=issue_data.dict(), headers=headers)

    if response.status_code == 201:
        print("Issue успешно создан!")
        return response.json()
    else:
        return {
            "status": response.status_code,
            "message": response.json().get("message", "Ошибка создания Issue")
        }


@mini_app.patch('/{owner}/{repo}/{issue_number}')
def close_github_issue(owner, repo, issue_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    close_data = {
        "state": "closed"
    }

    response = requests.patch(url, json=close_data, headers=headers)

    if response.status_code == 200:
        print("Issue успешно закрыт!")
        return response.json()
    else:
        return {
            "status": response.status_code,
            "message": response.json().get("message", "Ошибка закрытия Issue")
        }

def start():
    uvicorn.run(
        "server.main:mini_app",
        host=collection_host,
        port=collection_port,
        reload=True,
    )