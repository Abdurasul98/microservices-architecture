from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Post
from .schemas import PostCreate, PostResponse
import httpx

USER_SERVICE_URL = "http://127.0.0.1:8001/api/users"

router = APIRouter()

@router.get("/",response_model=list[PostResponse])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return posts

@router.post("/", response_model=PostResponse)
async def create_post(post: PostCreate, db: Session = Depends(get_db)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{USER_SERVICE_URL}/{post.user_id}/")

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="User topilmadi!")

    user = response.json()

    new_post = Post(
        title=post.title,
        content=post.content,
        user_id=post.user_id
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    result = PostResponse.from_orm(new_post)
    result.created_by = user
    return result

@router.get("/{post_id}/", response_model=PostResponse)
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post topilmadi!")
    return post