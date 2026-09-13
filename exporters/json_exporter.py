from exporter import Exporter
from models.post import Post
import json

class JsonExporter(Exporter):
    def __init__(self, filename):
        self.filename = filename
        self.posts = []

    def save(self):
        data = [
            {
                "url": post.url,
                "posted_at": post.posted_at.isoformat()
            }

            for post in self.posts
        ]

        with open(f"output/{self.filename}.json", "w", encoding="utf-8") as file:
            json.dump(
                data, 
                file, 
                ensure_ascii=False, 
                indent=4
            )

    def add(self, post: Post):
        self.posts.append(post)