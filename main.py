import instaloader
from datetime import datetime, timezone, timedelta

L = instaloader.Instaloader()

profile = instaloader.Profile.from_username(
    L.context,
    "hub4.bike"
)

limite = datetime.now(timezone.utc) - timedelta(days=90)

urls = []

for post in profile.get_posts():
    print(post.caption)
    print("\n---------------\n")

    post_date = post.date_utc.replace(tzinfo=timezone.utc)

    if post_date < limite:
        url = (
            f"https://www.instagram.com/"
            f"p/{post.shortcode}/"
        )

        urls.append(url)
        print(url)

print(f"\nTotal: {len(urls)} URLs")