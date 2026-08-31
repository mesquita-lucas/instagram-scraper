from session import Session
import os, sys
from dotenv import load_dotenv
import json

def main():
    load_dotenv()

    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")  
    
    if not username or not password:
        raise ValueError("Credenciais não cadastradas.")

    if len(sys.argv) < 2:
        raise ValueError("Informe o nome da página para proceder com a extração.")

    page_name = sys.argv[1]
    print(sys.argv[1], username, password)

    session = Session()

    session.login(
        username, 
        password
    )

    input("Siga o processo de autorização e/ou captcha até que você esteja completamente logado em sua conta. Então, aperte Enter.")

    posts = session.scrape(page_name)

    with open(f"posts_from_{page_name}.json", "w", encoding="utf-8") as arquivo:
        json.dump(posts, arquivo, ensure_ascii=False, indent=4)

    print(f"\nTotal coletado: {len(posts)}")

if __name__ == "__main__":
    main()