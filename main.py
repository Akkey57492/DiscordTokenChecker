import requests
import time
import re

print("""

████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
""")

tokens = open("tokens.txt", "r")
for token in tokens:
    result = token.replace("\n", "")
    Headers = {"authorization": f"{result}"}
    Check = requests.get("https://discordapp.com/api/v6/auth/login", headers=Headers)
    GetResponse = Check.json()
    Failed = GetResponse["message"]
    if Check.status_code == 200:
        print(f"ValidToken: {result}")
    elif Failed == "You are being rate limited.":
        print(f"Failed: {result}")
        print("一時的な制限がかかりました。")
        print("120秒後(2分後)に再開します。")
        time.sleep(120)
    else:
        print(f"InvalidToken: {result}")
