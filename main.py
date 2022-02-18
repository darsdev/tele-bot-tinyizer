import requests as r
import json as js
import pyrebase, firebase_admin, urllib
import time as t
from pyrebase.pyrebase import storage  
from firebase_admin import storage as admin_storage, credentials, firestore

#5075714498:AAFLg-y4SCEKk3PBEFEAjhl4FK5ViJMJvUE
id = 0
url = "https://api.telegram.org/bot5038867691:AAFM39l61cxZkBOfrI-6SVQfqEf7Z8xSV50/"
data = {
    "type":"article",
    "id":"1",
    "title": "a",
    "input_message_content": {"message_text": ""}
}
chars = [
    "ᵃ",
    "ᵇ",
    "ᶜ",
    "ᵈ",
    "ᵉ",
    "ᶠ",
    "ᵍ",
    "ʰ",
    "ⁱ",
    "ʲ",
    "k",
    "ˡ",
    "ᵐ",
    "ⁿ",
    "ᵒ",
    "ᵖ",
    "ᑫ",
    "ʳ",
    "ˢ",
    "ᵗ",
    "ᵘ",
    "ᵛ",
    "ʷ",
    "ˣ",
    "ʸ",
    "ᶻ",
    "¹",
    "²",
    "³",
    "⁴",
    "⁵",
    "⁶",
    "⁷",
    "⁸",
    "⁹",
    "⁰"
]

if js.loads(r.get(url + "getUpdates").text)["result"] != [] and "inline_query" in js.loads(r.get(url + "getUpdates").text)["result"][0]:
    id = int(js.loads(r.get(url + "getUpdates").text)["result"][0]["update_id"])

def recivedUpdate(queryId, content):
    if content != "":
        print(content)
        content.replace("b", "a")
        print(content)
        data["input_message_content"]["message_text"] = content
        data["title"] = content
        jsonData = js.dumps(data)
        params = {
            "inline_query_id": queryId,
            "results": '[' + str(jsonData) + ']'
        }
        req = r.get(url + "answerInlineQuery", params=params)
        print(req.url)
        print(req.text)

    else:
        exit

while True:
    updateReq = js.loads(r.get(url + "getUpdates").text)
    updateReqoff = js.loads(r.get(url + "getUpdates?offset=" + str(id)).text)["result"]
    if updateReq["result"] != []:
        if updateReqoff != []:
            if "inline_query" in updateReqoff[0]:
                #t.sleep(0.3)
                id = int(updateReq["result"][0]["update_id"]) + 1
                recivedUpdate(updateReq["result"][0]["inline_query"]["id"], updateReq["result"][0]["inline_query"]["query"])
                continue
            else:
                continue

        else:
            continue
    
    else:
        continue