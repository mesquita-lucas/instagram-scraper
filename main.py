from session import Session
import os
from dotenv import load_dotenv
import json

def main():
    session = Session()
    load_dotenv()
    
    session.login(
        os.getenv("USERNAME"), 
        os.getenv("PASSWORD")
    )

    input("Siga o processo de autorização e/ou captcha até que você esteja completamente logado em sua conta. Então, aperte Enter.")

    posts = session.scrape("hub4.bike")

    with open("posts_url.json", "w", encoding="utf-8") as arquivo:
        json.dump(posts, arquivo, ensure_ascii=False, indent=4)

    print(f"\nTotal coletado: {len(posts)}")

if __name__ == "__main__":
    main()