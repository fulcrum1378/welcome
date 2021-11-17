import os

from chameleon import PageTemplateFile, PageTemplateLoader

folder = "welcome"
temp = PageTemplateLoader(os.path.join(os.path.dirname(__file__), folder), encoding="utf-8")
# Chameleon doesn't support Persian characters!
print("Content-Type: text/html\n")
print(temp["temp.html"](**{
    "root": "/" + folder + "/",
    "page": "main",
    "favicon": "/mahdi/Images/fav-icon.ico",
    "title": "Mahdi Parastesh",
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
            "id": "mergen",
            "name": "Mergen",
            "desc": "A logical Artificial Intelligence software, an operating system for a robot.",
            "source": "https://github.com/fulcrum1378/mergen_android",
        },
        {
            "id": "mergen",
            "name": "AvaBot",
            "desc": "Speech Recognizer, Text-to-Speech and Optical Character Recognition for Persian and Turkic "
                    "languages",
            "source": "https://github.com/fulcrum1378/avabot-browser",
        },
        {
            "id": "telexporter",
            "name": "Telexporter",
            "desc": "Export your messages and call history to HTML, PDF or JSON files.",
            "source": "https://github.com/fulcrum1378/telexporter",
        },
        {
            "id": "migratio",
            "name": "Migratio",
            "desc": "Migratio Wordpress-powered website",
            "source": "https://github.com/fulcrum1378/migratio",
        },
        {
            "id": "migratio",
            "name": "Migratio (Android)",
            "desc": "A geographical statistical tool for determining someone's best destination for migration.",
            "source": "https://github.com/fulcrum1378/migratio_android",
            "target": "https://migratio.mahdiparastesh.ir/",
        },
        {
            "id": "sexbook",
            "name": "Sexbook",
            "desc": "Control your sexual life easily.",
            "source": "https://github.com/fulcrum1378/sexbook",
        },
        {
            "id": "friend_tracker",
            "name": "Friend Tracker",
            "desc": "Easily track your friends on the map.",
            "source": "https://github.com/fulcrum1378/friend_tracker"
        },
        {
            "id": "saam",
            "name": "Saam",
            "desc": "Stock market data collector based on MetaTrader5",
            "source": "https://github.com/fulcrum1378/saam",
        },
    ],
}))

# HTML Notes:
# <object data="${root}img/${s.icon}.svg" type="image/svg+xml"></object>
# Animated button must be put in an inner element; so that it won't drop out of its bounds!
