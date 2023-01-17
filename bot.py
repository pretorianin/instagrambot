from instagrapi import Client
import random


username = ""
password = ""

client = Client()
client.login(username, password)

hashtag = "programming"
comments = ["awesome", "nice", "good"]

medias = client.hashtag_medias_recent(hashtag, 20)

for i, media in enumerate(medias):
    client.media_like(media.id)
    print(f"liked pst number {i+1} of hashtag {hashtag}")
    if i % 5 == 0:
        client.user_follow(media.user.pk)
        print(f"Followed user{media.user.username}")
        client.media_comment(media.id,random.choce(comments))
        print(f"commented")



