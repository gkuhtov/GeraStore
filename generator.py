import json
from datetime import datetime

BASE = "https://gkuhtov.github.io/GeraStore/"

with open("apps/apps.json", "r", encoding="utf-8") as f:
    data = json.load(f)

apps = []

for app in data["apps"]:

    apps.append({
        "name": app["name"],
        "bundleIdentifier": app["bundleIdentifier"],
        "developerName": app["developerName"],
        "subtitle": app["subtitle"],
        "localizedDescription": app["description"],
        "iconURL": BASE + "icons/" + app["icon"],
        "category": app["category"],

        "screenshots": [],

        "versions": [
            {
                "version": app["version"],
                "date": datetime.utcnow().isoformat() + "Z",
                "downloadURL": BASE + "ipa/" + app["ipa"],
                "size": 0,
                "localizedDescription": "Последняя версия."
            }
        ]
    })


repo = {
    "name": "GeraStore",
    "identifier": "com.gkuhtov.gerastore",
    "subtitle": "IPA Repository",
    "description": "Каталог IPA приложений для GBox.",
    "iconURL": BASE + "icons/logo.png",
    "website": BASE,
    "sourceURL": BASE + "repo.json",
    "featuredApps": [],
    "news": [],
    "apps": apps
}


with open("repo.json", "w", encoding="utf-8") as f:
    json.dump(
        repo,
        f,
        indent=2,
        ensure_ascii=False
    )


print("repo.json создан")
