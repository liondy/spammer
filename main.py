from dotenv import load_dotenv
import os
import requests

def loadEnv():
    load_dotenv()
    global token
    global chat_id

    token = os.getenv("TOKEN")
    chat_id = os.getenv("CHATID")

def spammmmm(msg):
    endpoint = f"https://api.telegram.org/bot{token}/sendMessage?parse_mode=markdown&chat_id={chat_id}&text={msg}"
    response = requests.post(endpoint)
    try:
        response.raise_for_status()
        print(
            f"{response.content}")
    except requests.exceptions.HTTPError as e:
        print(f"{e}")

def main():
    loadEnv()
    for i in range(100000000000):
        spammmmm("GO AWAY!!")

if __name__ == "__main__":
    main()
