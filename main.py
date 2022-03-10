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
got = {"hl": ""}
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
        {
            "icon": "linktree",
            "link": "https://linktr.ee/fulcrum1378",
            "title": "Mahdi Parastesh | Linktree",
        },
    ],
    "projects": [
        {
            "id": "instatools",
            "name": "InstaTools",
            "desc": "Find unfollowers, download all saved posts, download any post and export DMs into PDF and HTML.",
            "anchors": [
                {
                    "name": "Google Play",
                    "link": "https://play.google.com/store/apps/details?id=ir.mahdiparastesh.instatools",
                    "title": ""
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.instatools",
                    "title": "Iranian Android Myket Store"
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.instatools",
                    "title": "Iranian Android Bazaar Store"
                },
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/instatools.html",
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
                    "name": "Website",
                    "link": "https://migratio.mahdiparastesh.ir/",
                    "title": ""
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.migratio",
                    "title": "Iranian Android Myket Store"
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.migratio",
                    "title": "Iranian Android Bazaar Store"
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
            "id": "mergen",
            "name": "Mergen",
            "desc": "A logical Artificial Intelligence software, an operating system for a robot.",
            "anchors": [
                {
                    "name": "Server Source",
                    "link": "https://github.com/fulcrum1378/mergen",
                    "title": ""
                },
                {
                    "name": "Android Source",
                    "link": "https://github.com/fulcrum1378/mergen_android",
                    "title": ""
                },
            ]
        },
        {
            "id": "telexporter",
            "name": "Telexporter",
            "desc": "Export your messages and call history to HTML, PDF or JSON files.",
            "anchors": [
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/telexporter.html",
                    "title": ""
                },
            ]
        },
        {
            "id": "fortuna",
            "name": "Fortuna",
            "desc": "An application of the Hedonist philosophy!",
            "anchors": [
                {
                    "name": "Flutter Source",
                    "link": "https://github.com/fulcrum1378/fortuna",
                    "title": ""
                },
            ]
        },
        {
            "id": "friend_tracker",
            "name": "Friend Tracker",
            "desc": "Easily track your friends on the map.",
            "anchors": [
                {
                    "name": "Android Source",
                    "link": "https://github.com/fulcrum1378/friend_tracker",
                    "title": ""
                },
            ]
        },
        {
            "id": "saam",
            "name": "Saam",
            "desc": "Stock market data collector based on MetaTrader5",
            "anchors": [
                {
                    "name": "Software Source",
                    "link": "https://github.com/fulcrum1378/saam",
                    "title": ""
                },
            ]
        },
    ],
}
print(temp["temp.html"](**data))

# HTML Notes:
# <object data="${root}img/${s.icon}.svg" type="image/svg+xml"></object>
# Animated button must be put in an inner element; so that it won't drop out of its bounds!
