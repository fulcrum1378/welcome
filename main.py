import cgi
import os

from chameleon import PageTemplateFile, PageTemplateLoader

folder = "welcome"
temp = PageTemplateLoader(os.path.join(os.path.dirname(__file__), folder), encoding="utf-8")
got = {"hl": "en"}
try:
    for g in cgi.FieldStorage().list: got[g.name] = g.value
except:
    pass
l = got["hl"]
print("Content-type: text/html\n")
print(temp["temp.html"](**{
    "root": "/" + folder + "/",
    "page": "main",
    "favicon": "/mahdi/Images/fav-icon.ico",
    "title": {
        "en": "Mahdi Parastesh",
        "fa": "مهدی پرستش"
    }[l],
    "header": {
        "en": "Mahdi Parastesh",
        "fa": "مهدی پرستش"
    }[l],
    "biography": {
        "en": """I have 6 years of experience in <b>Full-Stack software engineering</b>.<br><br>
    The programming languages I'm skilled in are JavaScript, PHP, Java, SQL, Kotlin, Dart, Python and Prolog.
    I can develop Android apps using mere Java/Kotlin, or also for iOS using Flutter or React Native.
    I also know Node.js, TensorFlow, PyTorch, MySQL and PostgreSQL.<br>
    I practice Machine Learning and I'm also an expert in Linux.""",
        "fa": """"""
    }[l],
    "social": [
        {
            "icon": "github",
            "link": "https://github.com/fulcrum1378",
            "title": "fulcrum1378 (Mahdi Parastesh) · GitHub",
        },
        {
            "icon": "linkedin-in",
            "link": "https://www.linkedin.com/in/mahdi-parastesh-a72ab51b9/",
            "title": "Mahdi Parastesh | LinkedIn",
        },
        {
            "icon": "stack-overflow",
            "link": "https://stackoverflow.com/users/10728785/mahdi-parastesh",
            "title": "User Mahdi Parastesh - Stack Overflow",
        },
        {
            "icon": "facebook-f",
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
    ],
    "projects": [
        {
            "id": "mergen",
            "name": {
                "en": "Mergen",
                "fa": "مِرگِن"
            }[l],
            "desc": {
                "en": "A logical Artificial Intelligence software, an operating system for a robot.",
                "fa": "یک نرم افزار هوش مصنوعی منطقی، سیستم عاملی برای یک ربات."
            }[l],
            "source": "https://github.com/fulcrum1378/mergen_android",
        },
        # {
        #    "id": "avabot",
        #    "name": "AvaBot",
        #    "desc": "Speech Recognizer, Text-to-Speech and Optical Character Recognition for Persian language",
        #    "source": "https://github.com/fulcrum1378/avabot-browser",
        # },
        {
            "id": "telexporter",
            "name": {
                "en": "Telexporter",
                "fa": "تلکسپورتر"
            }[l],
            "desc": {
                "en": "Export your messages and call history to HTML, PDF or JSON files.",
                "fa": "اس ام اس ها و تاریخچه تماس های خود را در قالب های وب، پی دی اف و جیسون استخراج کنید."
            }[l],
            "source": "https://github.com/fulcrum1378/telexporter",
        },
        {
            "id": "migratio",
            "name": {
                "en": "Migratio",
                "fa": "میگراتیو"
            }[l],
            "desc": {
                "en": "Migratio Wordpress-powered website",
                "fa": "وبسایت وردپرسی میگراتیو"
            }[l],
            "source": "https://github.com/fulcrum1378/migratio",
        },
        {
            "id": "migratio",
            "name": {
                "en": "Migratio (Android)",
                "fa": "میگراتیو (اندروید)"
            }[l],
            "desc": {
                "en": "A geographical statistical tool for determining someone's best destination for migration",
                "fa": "یک ابزار جغرافی-آماری برای تعیین کردن بهترین مقصد مهاجرت افراد مختلف"
            }[l],
            "source": "https://github.com/fulcrum1378/migratio_android",
            "target": "https://migratio.mahdiparastesh.ir/",
        },
        {
            "id": "sexbook",
            "name": {
                "en": "Sexbook",
                "fa": "سکسبوک"
            }[l],
            "desc": {
                "en": "Control your sexual life easily",
                "fa": "زندگی جنسی خود را به آسانی کنترل کنید"
            }[l],
            "source": "https://github.com/fulcrum1378/sexbook",
        },
        {
            "id": "friend_tracker",
            "name": {
                "en": "Friend Tracker",
                "fa": "ردیاب رفقا"
            }[l],
            "desc": {
                "en": "Easily track your friends on the map.",
                "fa": "رفقای خود را از روی نقشه ردیابی نمایید."
            }[l],
            "source": "https://github.com/fulcrum1378/friend_tracker"
        },
        {
            "id": "saam",
            "name": {
                "en": "Saam",
                "fa": "سام"
            }[l],
            "desc": {
                "en": "Stock market data collector based on MetaTrader5",
                "fa": "گرداور و ذخیره کننده اطلاعات بورس، ساخته شده بر مبنای متاتریدر 5"
            }[l],
            "source": "https://github.com/fulcrum1378/saam",
        },
    ],
}))

# HTML Notes:
# <object data="${root}img/${s.icon}.svg" type="image/svg+xml"></object>
# Animated button must be put in an inner element; so that it won't drop out of its bounds!
