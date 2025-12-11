from datetime import datetime, UTC
from typing import Annotated

from fastapi import FastAPI, status, Cookie, Response, Header, APIRouter
from pydantic import BaseModel, Field
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")

fake_db = [
    {"title": "Criando uma aplicação com Django", "date": datetime.now(UTC), "published": True},
    {"title": "Internacionalizando um app FastAPI", "date": datetime.now(UTC), "published": True},
    {"title": "Criando uma aplicação com Flask", "date": datetime.now(UTC), "published": True},
    {"title": "Internacionalizando um app Starleet", "date": datetime.now(UTC), "published": False},
]


class Foo(BaseModel):
    bar: str


@router.get("/foobar/", response_model=Foo)
def foobar() -> dict[str, str]:
    return {"bar": "foo", "message": "hello world"}



@router.post("/",  status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump())
    return post


@router.get("/", response_model=list[PostOut])
def read_posts(response: Response, skip: int = 0, limit: int = None, published: bool = True, ads_id: Annotated[str | None, Cookie()] = None,
            user_agent: Annotated[str | None, Header()] = None   ):
    

    response.set_cookie(key="user", value="tutuxiid@jadh.com.br")
    print(f"Cookie: {ads_id}")
    print(f"User-agent: {user_agent}")
    filtered = [post for post in fake_db if post["published"] == published]

    if limit is None:
        limit = len(filtered)
    return filtered[skip : skip + limit]


@router.get("/{framework}", response_model=PostOut)
def read_framework_posts(framework: str):
    return {
        "posts": [
            {"title": f"Criando uma aplicação com {framework}", "date": datetime.now(UTC)},
            {"title": f"Internacionalizando um app {framework}", "date": datetime.now(UTC)},
        ]
    }