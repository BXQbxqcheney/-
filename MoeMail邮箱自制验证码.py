import random
send_email=""
while "@" not in send_email:
    send_email=input("请输入邮箱：")
def send(send_email, title, word,id,cookie):
    import requests
    import time
    headers = {
        "authority": "moemail.app",
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-type": "application/json",
        "cookie": cookie,
        "origin": "https://moemail.app",
        "priority": "u=1, i",
        "referer": "https://moemail.app/moe",
        "sec-ch-ua": '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
    }
    send_url = f"https://moemail.app/api/emails/{id}/send"
    data = {
        "to": str(send_email),
        "subject": str(title),
        "content": str(word)
    }
    print("发送中...")
    send_response = requests.post(send_url, headers=headers, json=data)
    print(f"发送状态码: {send_response.status_code}",end="")
    if send_response.status_code==200:
        print("(发送成功)")
        print("请等待后续操作...")
        time.sleep(0.5)
        get_url = f"https://moemail.app/api/emails/{id}?type=sent"
        get_response = requests.get(get_url, headers=headers)
        if get_response.status_code == 200:
            try:
                emails_data = get_response.json()
                if emails_data.get("messages") and len(emails_data["messages"]) > 0:
                    email_id = emails_data["messages"][0]["id"]
                    delete_url = f"https://moemail.app/api/emails/{id}/{email_id}?type=sent"
                    requests.delete(delete_url, headers=headers)
            except ValueError:
                pass
        print("操作完毕！")
    else:
        print("发送失败！")
id=""
cookie=""
num=str(random.randint(12345678,99999999))
mold=f"您的验证码为：{num}，在校验前有效。如非本人操作，请忽略本邮件。本邮件由系统自动发出，请勿直接回复。"
send(send_email,"验证码",mold,id,cookie)
chat=0
while chat!=num:
    chat=input("验证码：")
    if chat!=num:
        print("重发：",end="")
        num = random.randint(12345678, 99999999)
        mold = f"您的验证码为：{num},注册码2分钟内有效。如非本人操作，请忽略本邮件该邮件由系统自动发出，请勿直接回复。"
        send(send_email, "验证码", mold, id, cookie)
print("验证成功！")