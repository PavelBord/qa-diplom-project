from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    username: str
    email: str
    role: str
    avatar_url: str | None = None
    created_at: str
