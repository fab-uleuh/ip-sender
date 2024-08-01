from requests import get, post
import json
import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def send_webhook(webhook_url, message):
    message = {"content": message}

    response = post(webhook_url, json=message)

    if response.status_code == 204:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")


with open(os.path.join(__location__, "config.json"), "r") as f:
    config = json.load(f)

ip = get("https://api.ipify.org").text

if ip != config["ip"]:
    
    last_ip = config["ip"]
    
    send_webhook(config["url_webhook"], f"Changement IP :{last_ip} --> {ip}  ")

    # write it back to the file
    config["ip"] = ip
    with open(os.path.join(__location__, "config.json"), "w") as f:
        json.dump(config, f)

