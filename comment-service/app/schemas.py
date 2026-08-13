from dataclasses import dataclass

@dataclass
class CommentCreate:
    content: str
    user_id: int
    post_id: int