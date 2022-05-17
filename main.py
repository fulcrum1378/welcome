import cgi
import os

import requests
from chameleon import PageTemplateLoader

folder = "welcome"
try:
    country = requests.get("https://geolocation-db.com/json/{}&position=true".format(os.environ["REMOTE_ADDR"])
                           ).json()["country_code"]
except:
    country = ""
got = {"hl": "", "fk": "0"}
try:
    for g in cgi.FieldStorage().list: got[g.name] = g.value
except:
    pass
temp = PageTemplateLoader(os.path.join(os.path.dirname(__file__), folder), encoding="utf-8")
# Chameleon doesn't support Persian characters!
print("Content-Type: text/html\n")
data = {
    "root": "/" + folder + "/",
    "page": "main",
    "favicon": "https://mahdi.mahdiparastesh.ir/Images/fav-icon.ico",
    "title": "Mahdi Parastesh",
    "country": country,
    "help": got["hl"],
    "social": [
        {
            "icon": "github",
            "link": "https://github.com/fulcrum1378",
            "title": "fulcrum1378 (Mahdi Parastesh) · GitHub",
        },
        {
            "icon": "linkedin",
            "link": "https://www.linkedin.com/in/mahdi-parastesh-a72ab51b9/",
            "title": "Mahdi Parastesh | LinkedIn",
        },
        {
            "icon": "google_play",
            "link": "https://play.google.com/store/apps/dev?id=8797895762316770334",
            "title": "Android Apps by Mahdi Parastesh on Google Play",
        },
        {
            "icon": "stackoverflow",
            "link": "https://stackoverflow.com/users/10728785/mahdi-parastesh",
            "title": "User Mahdi Parastesh - Stack Overflow",
        },
        {
            "icon": "facebook",
            "link": "https://www.facebook.com/mpg973",
            "title": "Mahdi Prs",
        },
        {
            "icon": "twitter",
            "link": "https://twitter.com/fulcrum1378",
            "title": "Mahdi Parastesh (@fulcrum1378) / Twitter",
        },
        {
            "icon": "instagram",
            "link": "https://www.instagram.com/fulcrum1378/",
            "title": "Mahdi Parastesh (@fulcrum1378) • Instagram photos and videos",
        },
        #{
        #    "icon": "linktree",
        #    "link": "https://linktr.ee/fulcrum1378",
        #    "title": "Mahdi Parastesh | Linktree",
        #},
    ],
    "projects": [
        {
            "id": "instatools",
            "name": "InstaTools",
            "desc": "Find unfollowers, download all saved posts, download any post and export DMs into HTML, PDF and TXT.",
            "anchors": [
                {
                    "name": "Google Play",
                    "link": "https://play.google.com/store/apps/details?id=ir.mahdiparastesh.instatools.beth",
                    "title": ""
                },
                {
                    "name": "Galaxy Store",
                    "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.instatools.beth",
                    "title": ""
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.instatools",
                    "title": "Iranian Android Bazaar Store"
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.instatools",
                    "title": "Iranian Android Myket Store"
                },
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/instatools.html",
                    "title": ""
                },
            ]
        },
        {
            "id": "telexporter",
            "name": "Telexporter",
            "desc": "Export your messages and call history to HTML, PDF or TXT files.",
            "anchors": [
                {
                    "name": "Galaxy Store",
                    "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.telexporter",
                    "title": ""
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.telexporter",
                    "title": "Iranian Android Bazaar Store"
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.telexporter",
                    "title": "Iranian Android Myket Store"
                },
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/telexporter.html",
                    "title": ""
                },
            ]
        },
        {
            "id": "migratio",
            "name": "Migratio",
            "desc": "A geographical statistical tool for determining someone's best destination for migration.",
            "anchors": [
                {
                    "name": "Google Play",
                    "link": "https://play.google.com/store/apps/details?id=ir.mahdiparastesh.migratio",
                    "title": ""
                },
                {
                    "name": "Galaxy Store",
                    "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.migratio",
                    "title": ""
                },
                {
                    "name": "Website",
                    "link": "https://migratio.mahdiparastesh.ir/",
                    "title": ""
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.migratio",
                    "title": "Iranian Android Bazaar Store"
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.migratio",
                    "title": "Iranian Android Myket Store"
                },
                {
                    "name": "Web Template",
                    "link": "https://github.com/fulcrum1378/migratio",
                    "title": "Wordpress Theme"
                },
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/migratio.html",
                    "title": ""
                },
            ]
        },
        {
            "id": "fortuna",
            "name": "Fortuna",
            "desc": "An experimental application of the Hedonist philosophy!",
            "anchors": [
                {
                    "name": "Download for Android",
                    "link": "https://github.com/fulcrum1378/fortuna/raw/master/app/release/app-release.apk",
                    "title": ""
                },
                {
                    "name": "Website",
                    "link": "https://fortuna.mahdiparastesh.ir/",
                    "title": ""
                },
                {
                    "name": "Android Source (Kotlin)",
                    "link": "https://github.com/fulcrum1378/fortuna",
                    "title": ""
                },
                {
                    "name": "Flutter Source",
                    "link": "https://github.com/fulcrum1378/fortuna_flutter",
                    "title": ""
                },
            ]
        },
        {
            "id": "mergen",
            "name": "Mergen",
            "desc": "A logical Artificial Intelligence software, an operating system for a robot. (archived project)",
            "anchors": [
                {
                    "name": "Server Source (Python)",
                    "link": "https://github.com/fulcrum1378/mergen",
                    "title": ""
                },
                {
                    "name": "Android Source (Kotlin)",
                    "link": "https://github.com/fulcrum1378/mergen_android",
                    "title": ""
                },
            ]
        },
        {
            "id": "friend_tracker",
            "name": "Friend Tracker",
            "desc": "Easily track your friends on the map. (archived project)",
            "anchors": [
                {
                    "name": "Android Source (Java)",
                    "link": "https://github.com/fulcrum1378/friend_tracker",
                    "title": ""
                },
            ]
        },
        {
            "id": "saam",
            "name": "Saam",
            "desc": "Stock market data collector based on MetaTrader5 (archived project)",
            "anchors": [
                {
                    "name": "Software Source (Python)",
                    "link": "https://github.com/fulcrum1378/saam",
                    "title": ""
                },
            ]
        },
    ],
}
if got["fk"] == "1":
    data["projects"].append({
        "id": "sexbook",
        "name": "Sexbook",
        "desc": "With this app, you can record any kind of sexual activities you had in the past and view their statistics, frequency, recency, etc.",
        "anchors": [
            {
                "name": "Google Play",
                "link": "https://play.google.com/store/apps/details?id=ir.mahdiparastesh.sexbook",
                "title": ""
            },
            {
                "name": "Galaxy Store",
                "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.sexbook",
                "title": ""
            },
            {
                "name": "Privacy Policy",
                "link": "https://mahdiparastesh.ir/welcome/privacy/sexbook.html",
                "title": ""
            },
        ]
    })
print(temp["temp.html"](**data))

# HTML Notes:
# <object data="${root}img/${s.icon}.svg" type="image/svg+xml"></object>
# Animated button must be put in an inner element; so that it won't drop out of its bounds!
