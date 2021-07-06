import os

from chameleon import PageTemplateFile, PageTemplateLoader

folder = "welcome"
temp = PageTemplateLoader(os.path.join(os.path.dirname(__file__), folder))
print("Content-type: text/html\n")
print(temp["temp.html"](**{
    "root": "/" + folder + "/",
    "page": "main",
    "favicon": "/mahdi/Images/fav-icon.ico",
    "title": "Mahdi Parastesh",
    "social": [
        {
            "icon": "github",
            "name": "GitHub",
            "link": "https://github.com/fulcrum1378",
            "title": "fulcrum1378 (Mahdi Parastesh) · GitHub",
        },
        {
            "icon": "linkedin-in",
            "name": "LinkedIn",
            "link": "https://www.linkedin.com/in/mahdi-parastesh-a72ab51b9/",
            "title": "Mahdi Parastesh | LinkedIn",
        },
        {
            "icon": "stack-overflow",
            "name": "StackOverflow",
            "link": "https://stackoverflow.com/users/10728785/mahdi-parastesh",
            "title": "User Mahdi Parastesh - Stack Overflow",
        },
        {
            "icon": "facebook-f",
            "name": "Facebook",
            "link": "https://www.facebook.com/mpg973",
            "title": "Mahdi Prs",
        },
        {
            "icon": "twitter",
            "name": "Twitter",
            "link": "https://twitter.com/fulcrum1378",
            "title": "Mahdi Parastesh (@fulcrum1378) / Twitter",
        },
        {
            "icon": "instagram",
            "name": "Instagram",
            "link": "https://www.instagram.com/fulcrum1378/",
            "title": "Mahdi Parastesh (@fulcrum1378) • Instagram photos and videos",
        },
    ],
    "projects": [
        {
            "id": "mergen",
            "name": "Mergen",
            "desc": "A logical Artificial Intelligence app, an operating system for a robot",
            "source": "https://github.com/fulcrum1378/mergen_android",
        },
        #{
        #    "id": "avabot",
        #    "name": "AvaBot",
        #    "desc": "Speech Recognizer, Text-to-Speech and Optical Character Recognition for Persian language",
        #    "source": "https://github.com/fulcrum1378/avabot-browser",
        #},
        {
            "id": "sms_exporter",
            "name": "SMS Exporter",
            "desc": "Export your messages to HTML, PDF or JSON files",
            "source": "https://github.com/fulcrum1378/sms_exporter",
        },
        {
            "id": "migratio",
            "name": "Migratio",
            "desc": "Migratio official Wordpress-powered website",
            "source": "https://github.com/fulcrum1378/migratio",
        },
        {
            "id": "migratio",
            "name": "Migratio (Android)",
            "desc": "A geographical statistical tool for determining someone's best destination for migration",
            "source": "https://github.com/fulcrum1378/migratio_android",
            "target": "https://migratio.mahdiparastesh.ir/",
        },
        {
            "id": "onani",
            "name": "Onani Counter",
            "desc": "",
            "source": "https://github.com/fulcrum1378/onani_counter",
        },
        {
            "id": "friend_tracker",
            "name": "Friend Tracker",
            "desc": "Friend Tracker, easily find your friends on the map",
            "source": "https://github.com/fulcrum1378/friend_tracker"
        },
        {
            "id": "saam",
            "name": "Saam",
            "desc": "Stock Market Data Collector based upon MetaTrader5",
            "source": "https://github.com/fulcrum1378/saam",
        },
    ],
}))
