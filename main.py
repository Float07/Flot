#https://api.telegram.org/bot<token>/METHOD_NAME
#1107398730:AAFmVSD0cLcJ8h8qXIRb-Sd6dqe9sJuRSvc
#https://api.telegram.org/bot1107398730:AAFmVSD0cLcJ8h8qXIRb-Sd6dqe9sJuRSvc/METHOD_NAME

import requests
import json

Paramet = {"offset": 0}
executing = True
while executing:
    URL = "https://api.telegram.org/bot1107398730:AAFmVSD0cLcJ8h8qXIRb-Sd6dqe9sJuRSvc/"
    updates = requests.get(url=URL+"getUpdates", params=Paramet)
    updatesJSON = updates.json()

    if updatesJSON["result"]!=[]:

        if "message" in updatesJSON["result"][0] and "text" in updatesJSON["result"][0]["message"]:#Se é uma mensagem de texto
            rText = updatesJSON["result"][0]["message"]["text"]

            if updatesJSON["result"][0]["message"]["chat"]["id"] == 1080820184:
                sendMessageParam = {"chat_id": -1001367341107,
                                    "text": rText,}
                sendMessage = requests.post(url=URL + "sendMessage", data=sendMessageParam)
                print(sendMessage)

            elif rText.lower() == "oi":
                sendMessageParam = {"chat_id": updatesJSON["result"][0]["message"]["chat"]["id"],
                                    "text": "Oi",
                                    "reply_to_message_id": updatesJSON["result"][0]["message"]["message_id"]}
                print(updatesJSON["result"][0]["message"]["from"]["first_name"])
                if updatesJSON["result"][0]["message"]["from"]["id"] == 735844467:
                    sendMessageParam = {"chat_id": updatesJSON["result"][0]["message"]["chat"]["id"],
                                    "text": "Você Não",
                                    "reply_to_message_id": updatesJSON["result"][0]["message"]["message_id"]}
                sendMessage = requests.post(url=URL + "sendMessage", data=sendMessageParam)

            elif rText.lower() == "tchau":
                sendMessageParam = {"chat_id": updatesJSON["result"][0]["message"]["chat"]["id"],
                                    "text": "Tchau.",
                                    "reply_to_message_id": updatesJSON["result"][0]["message"]["message_id"]}
                if updatesJSON["result"][0]["message"]["from"]["id"] == 735844467:
                    sendMessageParam = {"chat_id": updatesJSON["result"][0]["message"]["chat"]["id"],
                                        "text": "...",
                                        "reply_to_message_id": updatesJSON["result"][0]["message"]["message_id"]}
                sendMessage = requests.post(url=URL + "sendMessage", data=sendMessageParam)

            elif "/banmeireles" in rText.lower():
                startPollParam = {"chat_id": updatesJSON["result"][0]["message"]["chat"]["id"],
                                "question": "Devemos banir o Maureles?",
                                "options": json.dumps(["Sim", "Não", "Ban Meireles"]),
                                "is_anonymous": False}
                startPoll = requests.post(url=URL + "sendPoll", data=startPollParam)

            elif "/ban" in rText.lower():
                splitText = rText.split(' ', 1)
                if len(splitText) > 1:
                    name = splitText[1]
                    startPollParam = {"chat_id": updatesJSON["result"][0]["message"]["chat"]["id"],
                                     "question": "Devemos banir o " + name +'?',
                                     "options": json.dumps(["Sim", "Não", "Ban Meireles"]),
                                     "is_anonymous": False}
                    startPoll = requests.post(url=URL + "sendPoll", data=startPollParam)

            elif "/explode" in rText.lower():
                SendMessageParam = {"chat_id": updatesJSON["result"][0]["message"]["chat"]["id"],
                                    "text": "BOOOOOoooooom!💥"}
                if updatesJSON["result"][0]["message"]["from"]["first_name"].lower() == "andre":
                    SendMessageParam["text"] = "Você não pode acender bombas andré foi mal :("
                sendMessage = requests.post(url=URL + "sendMessage", data=SendMessageParam)


            print(updatesJSON["result"][0]['message'])

        # Avança para próxima mensagem
        Paramet["offset"] = updatesJSON["result"][0]["update_id"]+1
