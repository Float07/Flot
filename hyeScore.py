# estrutura: score=> {"user_id": USERID(int), "ois": "OIS", "Tchaus":"TCHAUS", "Totals": TOTALS(int)}

import requests
import json

URL = "https://api.telegram.org/"
file = open("key", 'r')
URL = URL + file.read()[:-1]
file.close()

def sortScore(scores):
    scores = sorted(scores, key=lambda i: i["totals"], reverse=True)
    return scores


def increaseScore(message, hye):  # hye=1>oi hye=2>tchau
    scores = []
    userId = message["from"]["id"]
    try:
        with open("hyeScore.json") as jsonFile:
            if jsonFile:
                scores = json.load(jsonFile)
    except FileNotFoundError:
        print("Arquivo não encontrado. criando.")

    index = -1  # -1 se o usuário ainda não estiver na lista
    for idx, score in enumerate(scores):
        if score["user_id"] == userId:
            index = idx

    if index != -1:
        if hye == 1:
            scores[index]["ois"] = scores[index]["ois"] + 1
        else:
            scores[index]["tchaus"] = scores[index]["tchaus"] + 1
        scores[index]["totals"] = scores[index]["totals"] + 1
    else:
        if hye == 1:
            newUser = {"user_id": userId,
                       "ois": 1,
                       "tchaus": 0,
                       "totals": 1}
        else:
            newUser = {"user_id": userId,
                       "ois": 0,
                       "tchaus": 1,
                       "totals": 1}
        scores.append(newUser)

    scores = sortScore(scores)
    with open("hyeScore.json", 'w') as jsonFile:
        json.dump(scores, jsonFile)


def print_scores(chat_command_id):
    with open("hyeScore.json") as jsonFile:
        scores = json.load(jsonFile)
        complete_message = ""
        for idx, score in enumerate(scores):
            chat_param = {"chat_id": score["user_id"]}
            get_chat = requests.get(url=URL + "getChat", params=chat_param)
            chat_json = get_chat.json()
            if chat_json['ok']:
                complete_message = complete_message + str(idx) + "- " + chat_json["result"]["first_name"] + " " +\
                    chat_json["result"]["last_name"] + "=> " + "Ois:" + str(score["ois"]) + "  Tchaus:" +\
                    str(score["tchaus"]) + "  Totals:" + str(score["totals"]) + "\n"
            else:
                print(score["user_id"])

        message_param = {"chat_id": chat_command_id,
                         "text": complete_message}
        requests.post(url=URL + "sendMessage", data=message_param)
