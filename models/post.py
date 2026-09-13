from dataclasses import dataclass
from datetime import datetime

@dataclass
class Post():
    url: str
    posted_at: datetime