import requests

print("Tokenが有効か確認する場合はTokenの入力で確認したいTokenを入力してください。")
print("プログラムを終了する場合はTokenの入力で「exit」と入力してください。")
input("続行する場合はエンターキーを押してください。")

while True:
    token = input("Token: ")
    if token == "exit":
        exit()
    TokenVerify = requests.get('https://discordapp.com/api/v6/auth/login', headers={"authorization": token})
    if TokenVerify.status_code == 200:
        print()
        print('=== 確認結果 ===')
        print(f"Token: {token}")
        print("結果: 有効")
    else:
        print()
        print("=== 確認結果 ===")
        print(f"Token: {token}")
        print("結果: 無効")
    print()