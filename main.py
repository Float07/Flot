#https://api.telegram.org/bot<token>/METHOD_NAME
#1107398730:AAFmVSD0cLcJ8h8qXIRb-Sd6dqe9sJuRSvc
#https://api.telegram.org/bot1107398730:AAGG_FXoQ713wj-KT8iNJxzawugN_dgd9ls/METHOD_NAME

import numpy as np
import hyeScore as hye
import requests
import json
import time


Paramet = {"offset": 0}
executing = True
URL = "https://api.telegram.org/"
file = open("key", 'r')
URL = URL + file.read()[:-1]
file.close()

def processMessage(message):
    if "message" in message and "text" in message[
        "message"]:  # Se é uma mensagem de texto
        rText = message["message"]["text"]

        if message["message"]["chat"]["id"] == 1080820184 or message["message"]["chat"]["id"] == 735844467:
            if rText == "!CLSE":
                return "user_close"
            sendMessageParam = {"chat_id": -1001367341107,
                                "text": rText, }
            sendMessage = requests.post(url=URL + "sendMessage", data=sendMessageParam)
            print(sendMessage)

        elif rText.lower() == "oi":
            sendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                "text": "Oi",
                                "reply_to_message_id": message["message"]["message_id"]}
            if message["message"]["from"]["id"] == 735844467:
                sendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                    "text": "Você Não",
                                    "reply_to_message_id": message["message"]["message_id"]}
            sendMessage = requests.post(url=URL + "sendMessage", data=sendMessageParam)
            hye.increaseScore(message["message"], 1)

        elif rText.lower() == "tchau":
            sendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                "text": "Tchau.",
                                "reply_to_message_id": message["message"]["message_id"]}
            if message["message"]["from"]["id"] == 735844467:
                sendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                    "text": "...",
                                    "reply_to_message_id": message["message"]["message_id"]}
            sendMessage = requests.post(url=URL + "sendMessage", data=sendMessageParam)
            hye.increaseScore(updatesJSON["result"][0]["message"], 2)

        elif rText.lower() == "obrigado bot":
            sendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                "text": "Tamo junto. Precisando aí só chamar :)",
                                "reply_to_message_id": message["message"]["message_id"]}
            if message["message"]["from"]["id"] == 735844467:
                sendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                    "text": "É...",
                                    "reply_to_message_id": message["message"]["message_id"]}
            sendMessage = requests.post(url=URL + "sendMessage", data=sendMessageParam)

        elif "/tchoiscore" in rText.lower():
            hye.print_scores(message['message']["chat"]["id"])

        elif "/banmeireles" in rText.lower():
            startPollParam = {"chat_id": message["message"]["chat"]["id"],
                              "question": "Devemos banir o Maureles?",
                              "options": json.dumps(["Sim", "Não", "Ban Meireles"]),
                              "is_anonymous": False}
            startPoll = requests.post(url=URL + "sendPoll", data=startPollParam)

        elif "/ban" in rText.lower():
            splitText = rText.split(' ', 1)
            if len(splitText) > 1:
                name = splitText[1]
                startPollParam = {"chat_id": message["message"]["chat"]["id"],
                                  "question": "Devemos banir o " + name + '?',
                                  "options": json.dumps(["Sim", "Não", "Ban Meireles"]),
                                  "is_anonymous": False}
                startPoll = requests.post(url=URL + "sendPoll", data=startPollParam)

        elif "/questionario?tendencioso=on" in rText.lower():
            splitText = rText.split(' ', 1)
            if len(splitText) > 1:
                name = splitText[1]
                startPollParam = {"chat_id": message["message"]["chat"]["id"],
                                  "question": name,
                                  "options": json.dumps(["Sim", "Não, e eu sou idiota"]),
                                  "is_anonymous": False}
                startPoll = requests.post(url=URL + "sendPoll", data=startPollParam)

        elif "/questionario" in rText.lower():
            splitText = rText.split(' ', 1)
            if len(splitText) > 1:
                name = splitText[1]
                startPollParam = {"chat_id": message["message"]["chat"]["id"],
                                  "question": name,
                                  "options": json.dumps(["Sim", "Não", "Acho que sim mas sei lá :/","Talvez", "Não sei"]),
                                  "is_anonymous": False}
                startPoll = requests.post(url=URL + "sendPoll", data=startPollParam)

        elif "/explode" in rText.lower():
            SendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                "text": "BOOOOOoooooom!💥"}
            if message["message"]   ["from"]["first_name"].lower() == "andre":
                SendMessageParam["text"] = "Você não pode acender bombas andré foi mal :("
            sendMessage = requests.post(url=URL + "sendMessage", data=SendMessageParam)

        elif "/shrekscript" in rText.lower():
            shrekScriptFile = open('sscript.txt', mode='r')
            shrekScript = shrekScriptFile.read()
            shrekScript = shrekScript[:4000]
            shrekScriptFile.close()
            SendMessageParam = {"chat_id": message["message"]["chat"]["id"],
                                "text": shrekScript}
            if message["message"]   ["from"]["first_name"].lower() == "andre":
                SendMessageParam["text"] = "SOMEBODY ONCE TOLD ME"
            sendMessage = requests.post(url=URL + "sendMessage", data=SendMessageParam)

        print(message['message'])

while executing:
    updates = requests.get(url=URL+"getUpdates", params=Paramet)
    updatesJSON = updates.json()

    time.sleep(2)
    if updatesJSON["result"]:#Se tiver mensagem ainda não lida
        for message in updatesJSON["result"]:
            # Avança para próxima mensagem
            if (processMessage(message)) == "user_close":
                executing = False
                print("Finalizando processo por ordem do usuário")
            Paramet["offset"] = message["update_id"] + 1
