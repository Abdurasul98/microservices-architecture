from fastapi import APIRouter
from .views import router as post_router

router = APIRouter()
router.include_router(post_router, prefix="/posts", tags=["Posts"])