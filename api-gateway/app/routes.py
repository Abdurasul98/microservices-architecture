from fastapi import APIRouter, Request
from .proxy import forward_request
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

USER_SERVICE = "http://127.0.0.1:8001/api/users"
POST_SERVICE = "http://127.0.0.1:8002/api/posts"
COMMENT_SERVICE = "http://127.0.0.1:8003/api/comments"


class UserCreate(BaseModel):
    name: str
    email: str

class PostCreate(BaseModel):
    title: str
    content: str
    user_id: int

class CommentCreate(BaseModel):
    content: str
    user_id: int
    post_id: int

# User endpoints
@router.get("/users/", name="users_list", tags=["Users"])
async def users_list_gateway(request: Request):
    return await forward_request(f"{USER_SERVICE}/", request)

@router.post("/users/", name="users_create", tags=["Users"])
async def users_create_gateway(body: UserCreate, request: Request):
    return await forward_request(f"{USER_SERVICE}/", request)

@router.get("/users/{path:path}", name="user_detail", tags=["Users"])
async def user_detail_gateway(path: str, request: Request):
    return await forward_request(f"{USER_SERVICE}/{path}", request)

# Post endpoints
@router.get("/posts/", name="posts_list", tags=["Posts"])
async def posts_list_gateway(request: Request):
    return await forward_request(f"{POST_SERVICE}/", request)

@router.post("/posts/", name="posts_create", tags=["Posts"])
async def posts_create_gateway(body: PostCreate, request: Request):
    return await forward_request(f"{POST_SERVICE}/", request)

@router.get("/posts/{path:path}", name="post_detail", tags=["Posts"])
async def post_detail_gateway(path: str, request: Request):
    return await forward_request(f"{POST_SERVICE}/{path}", request)

# Comment endpoints
@router.get("/comments/", name="comments_list", tags=["Comments"])
async def comments_list_gateway(request: Request):
    return await forward_request(f"{COMMENT_SERVICE}/", request)

@router.post("/comments/", name="comments_create", tags=["Comments"])
async def comments_create_gateway(body: CommentCreate, request: Request):
    return await forward_request(f"{COMMENT_SERVICE}/", request)

@router.get("/comments/{path:path}", name="comment_detail", tags=["Comments"])
async def comment_detail_gateway(path: str, request: Request):
    return await forward_request(f"{COMMENT_SERVICE}/{path}", request)