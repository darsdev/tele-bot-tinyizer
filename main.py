import requests as r
import json as js
import time as t

#5075714498:AAFLg-y4SCEKk3PBEFEAjhl4FK5ViJMJvUE
id = 0
mesId = 0
URL = "https://api.telegram.org/bot5038867691:AAFM39l61cxZkBOfrI-6SVQfqEf7Z8xSV50/"
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

updateReqoffParams = {
    "offset": "0",
    "allowed_updates": ["inline_query"]
}

updateReqoffMessageParams = {
    "offset": "0",
    "allowed_updates": ["message"]
}

if js.loads(r.get(URL + "getUpdates").text)["result"] != []:
    id = int(js.loads(r.get(URL + "getUpdates").text)["result"][0]["update_id"])

def recivedUpdate(queryId, content):
    if content != "":
        content = content.replace("a", chars[0])
        content = content.replace("A", chars[1])

        content = content.replace("b", chars[1])
        content = content.replace("B", chars[1])
        
        content = content.replace("c", chars[2])
        content = content.replace("C", chars[2])
        
        content = content.replace("d", chars[3])
        content = content.replace("D", chars[3])
        
        content = content.replace("e", chars[4])
        content = content.replace("E", chars[4])
        
        content = content.replace("f", chars[5])
        content = content.replace("F", chars[5])
        
        content = content.replace("g", chars[6])
        content = content.replace("G", chars[6])
        
        content = content.replace("h", chars[7])
        content = content.replace("H", chars[7])
        
        content = content.replace("i", chars[8])
        content = content.replace("I", chars[8])
        
        content = content.replace("j", chars[9])
        content = content.replace("J", chars[9])
        
        content = content.replace("k", chars[10])
        content = content.replace("K", chars[10])
        
        content = content.replace("l", chars[11])
        content = content.replace("L", chars[11])
        
        content = content.replace("m", chars[12])
        content = content.replace("M", chars[12])
        
        content = content.replace("n", chars[13])
        content = content.replace("N", chars[13])
        
        content = content.replace("o", chars[14])
        content = content.replace("O", chars[14])
        
        content = content.replace("p", chars[15])
        content = content.replace("P", chars[15])
        
        content = content.replace("q", chars[16])
        content = content.replace("Q", chars[16])
        
        content = content.replace("r", chars[17])
        content = content.replace("R", chars[17])
        
        content = content.replace("s", chars[18])
        content = content.replace("S", chars[18])
        
        content = content.replace("t", chars[19])
        content = content.replace("T", chars[19])
        
        content = content.replace("u", chars[20])
        content = content.replace("U", chars[20])
        
        content = content.replace("v", chars[21])
        content = content.replace("V", chars[21]) 
         
        content = content.replace("w", chars[22])
        content = content.replace("W", chars[22])
          
        content = content.replace("x", chars[23])
        content = content.replace("X", chars[23])
         
        content = content.replace("y", chars[24])
        content = content.replace("Y", chars[24])
         
        content = content.replace("z", chars[25])
        content = content.replace("Z", chars[25])
         
        content = content.replace("1", chars[26])
         
        content = content.replace("2", chars[27])
         
        content = content.replace("3", chars[28])
         
        content = content.replace("4", chars[29])
         
        content = content.replace("5", chars[30])
         
        content = content.replace("6", chars[31])
         
        content = content.replace("7", chars[32])
         
        content = content.replace("8", chars[33])

        content = content.replace("9", chars[34])
        
        content = content.replace("0", chars[35])
        
        data["input_message_content"]["message_text"] = content
        data["title"] = content
        jsonData = js.dumps(data)
        params = {
            "inline_query_id": queryId,
            "results": '[' + str(jsonData) + ']'
        }
        req = r.get(URL + "answerInlineQuery", params=params)
        print(req.URL)
        print(req.text)

    else: exit

while True:
    updateReq = js.loads(r.get(URL + "getUpdates").text)
    updateReqoffParams["offset"] = str(id)
    updateReqoff = js.loads(r.get(URL + "getUpdates", params=updateReqoffParams).text)["result"]
    updateReqoffMessageParams["offset"] = str(mesId)
    updateReqoffMessage = js.loads(r.get(URL + "getUpdates", params=updateReqoffMessageParams).text)["result"]
    if updateReq["result"] != []:
        if updateReqoff != []:
            if "inline_query" in updateReqoff[0]:
                id = int(updateReqoff[0]["update_id"]) + 1
                t.sleep(0.1)
                if js.loads(r.get(URL + "getUpdates?offset=" + str(id)).text)["result"] == []:
                    recivedUpdate(updateReqoff[0]["inline_query"]["id"], updateReqoff[0]["inline_query"]["query"])
                continue
            elif "message" in updateReqoffMessage[0]:
                if "text" in updateReqoffMessage[0]["message"]:
                    if updateReqoffMessage[0]["message"]["text"] == "/start":
                        mesId = int(updateReqoffMessage[0]["update_id"]) + 1
                        senId = updateReqoffMessage[0]["message"]["from"]["id"]
                        dataj = {
                            "chat_id": senId,
                            "text": "Start Using the Bot In Inline Mode like This- @TinyizerBot enter any text here"
                        }
                        print(r.get(URL + "sendMessage", params=dataj).URL)
                        continue

                    elif updateReqoffMessage[0]["message"]["text"] == "/help":
                        mesId = int(updateReqoffMessage[0]["update_id"]) + 1
                        senId = updateReqoffMessage[0]["message"]["from"]["id"]
                        dataj = {
                            "chat_id": senId,
                            "text": "Start Using the Bot In Inline Mode like This- @TinyizerBot enter any text here"
                        }
                        print(r.get(URL + "sendMessage", params=dataj).URL)
                        continue

                    elif updateReqoffMessage[0]["message"]["text"] == "/settings":
                        mesId = int(updateReqoffMessage[0]["update_id"]) + 1
                        senId = updateReqoffMessage[0]["message"]["from"]["id"]
                        dataj = {
                            "chat_id": senId,
                            "text": "Never Gonna Give You Up, Never Gonna Let You Down"
                        }
                        print(r.get(URL + "sendMessage", params=dataj).URL)
                        continue
                    else: continue
                else: continue
            else: continue
        else: continue
    else: continue