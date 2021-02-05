import urllib.request
import os
import json

def download_version():
    with urllib.request.urlopen("https://github.com/Glowman554/MinecraftClone/releases/download/latest/version.txt") as response:
        version = response.read()
    return version.decode()

def get_loacl_version():
    try:
        with open("version.txt") as file:
            version = file.read()
        return version
    except:
        return "0"

def update_done():
    with open("version.txt", "w") as file:
        file.write(download_version())

def download_game(report_hook):
    urllib.request.urlretrieve("https://github.com/Glowman554/MinecraftClone/releases/download/latest/desktop-1.0.jar", "game.jar", reporthook=report_hook)

def launch_game(username):
    os.popen(f"java -jar game.jar name={username}")

def launch_game_server(username, host, port):
    os.popen(f"java -jar game.jar name={username} host={host} port={port} online")

def save_user_name(username):
    text = json.dumps({
        "username": username
    })

    with open("user.json", "w") as file:
        file.write(text)
        file.flush()

def save_server(host, port, online):
    text = json.dumps({
        "host": host,
        "port": port,
        "online": online
    })

    with open("server.json", "w") as file:
        file.write(text)
        file.flush()

def load_username():
    with open("user.json") as file:
        data = file.read()
    return json.loads(data)["username"]

def load_server():
    with open("server.json") as file:
        data = file.read()
    return json.loads(data)