from session import Session
import os, sys
from dotenv import load_dotenv

from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta

from exporters.json_exporter import JsonExporter

def main():
    load_dotenv()

    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")  
    
    if not username or not password:
        raise ValueError("Credenciais não cadastradas.")

    if len(sys.argv) < 2:
        raise ValueError("Informe o nome da página para proceder com a extração.")

    page_name = sys.argv[1]

    session = Session()
    exporter = JsonExporter(f"posts_from_{page_name}")

    now = datetime.now(timezone.utc)
    three_months_ago = now - relativedelta(months=3)

    session.login(
        username, 
        password
    )

    input("Siga o processo de autorização e/ou captcha até que você esteja completamente logado em sua conta. Então, aperte Enter.")

    for post in session.scrape(page_name):
        if post.posted_at < three_months_ago:
            exporter.add(post)

    exporter.save()

if __name__ == "__main__":
    main()