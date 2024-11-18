from pydantic import BaseModel


class IssueData(BaseModel):
    title: str
    body: str = None
    assignees: list[str] = None
    labels: list[str] = None