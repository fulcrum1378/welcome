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
# Chameleon supports neither Persian nor Cyrillic characters!
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
            "id": "mergen4",
            "icon": "mergen",
            "name": "Mergen IV",
            "desc": "A logical multi-sensed artificially intelligent robot (AIR) software. Temporarily designed for Android.",
            "anchors": [
                {
                    "name": "Android Source",
                    "link": "https://github.com/fulcrum1378/mergen_android",
                    "title": "",
                    "microType": "sameAs",
                },
            ],
            "microType": "SoftwareApplication",
            "os": "Android",
            "category": "AI, Logic, Robot",
        },
        {
            "id": "instatools",
            "icon": "instatools",
            "name": "InstaTools",
            "desc": "Find unfollowers, download all saved posts, download any post and export DMs into HTML, PDF and TXT.",
            "anchors": [
                {
                    "name": "Google Play",
                    "link": "https://play.google.com/store/apps/details?id=ir.mahdiparastesh.instatools.beth",
                    "title": "",
                    "microType": "installUrl",
                },
                {
                    "name": "Galaxy Store",
                    "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.instatools.beth",
                    "title": "",
                    "microType": "installUrl",
                },
                {
                    "name": "NashStore",
                    "link": "https://store.nashstore.ru/store/6295e2d7fb3ed3bb471ff674",
                    "title": "Russian App Store",
                    "microType": "installUrl",
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.instatools",
                    "title": "Iranian Android Bazaar Store",
                    "microType": "installUrl",
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.instatools",
                    "title": "Iranian Android Myket Store",
                    "microType": "installUrl",
                },
                {
                    "name": "APKPure",
                    "link": "https://apkpure.com/p/ir.mahdiparastesh.instatools.beth",
                    "title": "APKPure.com a third-party APK store",
                    "microType": "installUrl",
                },
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/instatools.html",
                    "title": "",
                    "microType": "publishingPrinciples",
                },
            ],
            "microType": "MobileApplication",
            "os": "Android",
            "category": "Tools, Personalisation",
        },
        {
            "id": "telexporter",
            "icon": "telexporter",
            "name": "Telexporter",
            "desc": "Export your messages and call history to HTML, PDF or TXT files.",
            "anchors": [
                {
                    "name": "Galaxy Store",
                    "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.telexporter",
                    "title": "",
                    "microType": "installUrl",
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.telexporter",
                    "title": "Iranian Android Bazaar Store",
                    "microType": "installUrl",
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.telexporter",
                    "title": "Iranian Android Myket Store",
                    "microType": "installUrl",
                },
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/telexporter.html",
                    "title": "",
                    "microType": "publishingPrinciples",
                },
            ],
            "microType": "MobileApplication",
            "os": "Android",
            "category": "Tools",
        },
        {
            "id": "migratio",
            "icon": "migratio",
            "name": "Migratio",
            "desc": "A geographical statistical tool for determining someone's best destination for migration.",
            "anchors": [
                {
                    "name": "Google Play",
                    "link": "https://play.google.com/store/apps/details?id=ir.mahdiparastesh.migratio",
                    "title": "",
                    "microType": "installUrl",
                },
                {
                    "name": "Galaxy Store",
                    "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.migratio",
                    "title": "",
                    "microType": "installUrl",
                },
                {
                    "name": "Website",
                    "link": "https://migratio.mahdiparastesh.ir/",
                    "title": "",
                    "microType": "sameAs",
                },
                {
                    "name": "Bazaar",
                    "link": "https://cafebazaar.ir/app/ir.mahdiparastesh.migratio",
                    "title": "Iranian Android Bazaar Store",
                    "microType": "installUrl",
                },
                {
                    "name": "Myket",
                    "link": "https://myket.ir/app/ir.mahdiparastesh.migratio",
                    "title": "Iranian Android Myket Store",
                    "microType": "installUrl",
                },
                {
                    "name": "Web Template",
                    "link": "https://github.com/fulcrum1378/migratio",
                    "title": "Wordpress Theme",
                    "microType": "url",
                },
                {
                    "name": "Privacy Policy",
                    "link": "https://mahdiparastesh.ir/welcome/privacy/migratio.html",
                    "title": "",
                    "microType": "publishingPrinciples",
                },
            ],
            "microType": "SoftwareApplication",
            "os": "Android, Web",
            "category": "Tools, Travel, Migration",
        },
        {
            "id": "fortuna",
            "icon": "fortuna",
            "name": "Fortuna",
            "desc": "An application of the Hedonist philosophy!",
            "anchors": [
                {
                    "name": "Download for Android (Gregorian calendar)",
                    "link": "https://github.com/fulcrum1378/fortuna/raw/master/app/gregorian/release/app-gregorian-release.apk",
                    "title": "",
                    "microType": "downloadUrl",
                },
                {
                    "name": "Download for Android (Persian calendar)",
                    "link": "https://github.com/fulcrum1378/fortuna/raw/master/app/persian/release/app-persian-release.apk",
                    "title": "",
                    "microType": "downloadUrl",
                },
                {
                    "name": "Website (Demo)",
                    "link": "https://fortuna.mahdiparastesh.ir/",
                    "title": "",
                    "microType": "sameAs",
                },
                {
                    "name": "Android Source (Kotlin)",
                    "link": "https://github.com/fulcrum1378/fortuna",
                    "title": "",
                    "microType": "url",
                },
                {
                    "name": "Flutter Source",
                    "link": "https://github.com/fulcrum1378/fortuna_flutter",
                    "title": "",
                    "microType": "url",
                },
            ],
            "microType": "SoftwareApplication",
            "os": "Android, Web, iOS",
            "category": "Philosophy, Lifestyle, Events, Health",
        },
        {
            "id": "mergen3",
            "icon": "mergen",
            "name": "Mergen III",
            "desc": "A multi-sensed artificially intelligent robot (AIR) software, which needed a server and (a) client(s). It was replaced by one which didn't need server and client. (archived project)",
            "anchors": [
                {
                    "name": "Server Source (Python)",
                    "link": "https://github.com/fulcrum1378/mergen_server",
                    "title": "",
                    "microType": "sameAs",
                },
                {
                    "name": "Android Source (Kotlin)",
                    "link": "https://github.com/fulcrum1378/mergen_client",
                    "title": "",
                    "microType": "url",
                },
            ],
            "microType": "SoftwareApplication",
            "os": "Android, Windows, Linux, macOS",
            "category": "Artificial Intelligence, AI, Logic, NLP",
        },
        {
            "id": "mergen2",
            "icon": "mergen_red",
            "name": "Mergen II (Pronouncer)",
            "desc": "An auditory (talking and hearing) NLP software robot. It was replaced by a auditory-visual software AI robot. (archived project)",
            "anchors": [
                {
                    "name": "Server Source (Python)",
                    "link": "https://github.com/fulcrum1378/pronouncer",
                    "title": "",
                    "microType": "sameAs",
                },
                {
                    "name": "Android Source (Kotlin)",
                    "link": "https://github.com/fulcrum1378/mergen_client",
                    "title": "",
                    "microType": "url",
                },
            ],
            "microType": "SoftwareApplication",
            "os": "Android, Windows, Linux, macOS",
            "category": "Artificial Intelligence, AI, Logic, NLP",
        },
        {
            "id": "mergen1",
            "icon": "mergen",
            "name": "Mergen I",
            "desc": "An NLP logical artificial intelligence software, aimed to think using pure digital text. It was replaced by an auditory one. (archived project)",
            "anchors": [
                {
                    "name": "Software Source (Python)",
                    "link": "https://github.com/fulcrum1378/mergen_server",
                    "title": "",
                    "microType": "sameAs",
                },
            ],
            "microType": "SoftwareApplication",
            "os": "Android, Windows, Linux, macOS",
            "category": "Artificial Intelligence, AI, Logic, NLP",
        },
        {
            "id": "friend_tracker",
            "icon": "friend_tracker",
            "name": "Friend Tracker",
            "desc": "Easily track your friends on the map. (archived project)",
            "anchors": [
                {
                    "name": "Android Source (Java)",
                    "link": "https://github.com/fulcrum1378/friend_tracker",
                    "title": "",
                    "microType": "sameAs",
                },
            ],
            "microType": "MobileApplication",
            "os": "Android",
            "category": "Maps & Navigation, Communication, Social",
        },
        {
            "id": "saam",
            "icon": "saam",
            "name": "Saam",
            "desc": "Stock market data collector based on MetaTrader5 (archived project)",
            "anchors": [
                {
                    "name": "Software Source (Python)",
                    "link": "https://github.com/fulcrum1378/saam",
                    "title": "",
                    "microType": "sameAs",
                },
            ],
            "microType": "SoftwareApplication",
            "os": "Windows",
            "category": "Finance, Business, Tools",
        },
    ],
}
if got["fk"] == "1":
    data["projects"].append({
        "id": "sexbook",
        "icon": "sexbook",
        "name": "Sexbook",
        "desc": "With this app, you can record any kind of sexual activities you had in the past and view their statistics, frequency, recency, etc.",
        "anchors": [
            {
                "name": "Google Play",
                "link": "https://play.google.com/store/apps/details?id=ir.mahdiparastesh.sexbook",
                "title": "",
                "microType": "installUrl",
            },
            {
                "name": "Galaxy Store",
                "link": "https://galaxystore.samsung.com/detail/ir.mahdiparastesh.sexbook",
                "title": "",
                "microType": "installUrl",
            },
            #{
            #    "name": "NashStore",
            #    "link": "<TODO>",
            #    "title": "<TODO>",
            #    "microType": "installUrl",
            #},
            {
                "name": "APKPure",
                "link": "https://apkpure.com/p/ir.mahdiparastesh.sexbook",
                "title": "APKPure.com a third-party APK store",
                "microType": "installUrl",
            },
            {
                "name": "Privacy Policy",
                "link": "https://mahdiparastesh.ir/welcome/privacy/sexbook.html",
                "title": "",
                "microType": "publishingPrinciples",
            },
        ],
        "microType": "MobileApplication",
        "os": "Android",
        "category": "Lifestyle, Events, Dating",
    })
print(temp["temp.html"](**data))

# HTML Notes:
# <object data="${root}img/${s.icon}.svg" type="image/svg+xml"></object>
# Animated button must be put in an inner element; so that it won't drop out of its bounds!
