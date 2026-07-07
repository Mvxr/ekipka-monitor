import requests
import re
import json


URL = "https://forum.devgaming.pl/topic/5-ekipa-devgaming-liderzy-frakcji/"


html = requests.get(
    URL,
    headers={
        "User-Agent":"Mozilla/5.0"
    }
).text



users=[]


profiles = re.findall(
    r'<a href="(https://forum\.devgaming\.pl/profile/[^"]+)"[^>]*>(.*?)</a>',
    html,
    re.S
)



for profile, content in profiles:


    name = re.sub(
        "<.*?>",
        "",
        content
    ).strip()



    start = html.find(profile)


    fragment = html[
        start-800:
        start+800
    ]



    avatar_match = re.search(
        r'<img[^>]+src="([^"]+)"',
        fragment
    )



    avatar = (
        avatar_match.group(1)
        if avatar_match
        else
        "https://forum.devgaming.pl/uploads/monthly_2023_01/default.png"
    )



    users.append({

        "name":name,

        "profile":profile,

        "avatar":avatar

    })




unique = {}


for user in users:

    unique[user["profile"]] = user



with open(
    "staff.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        list(unique.values()),
        f,
        ensure_ascii=False,
        indent=4
    )