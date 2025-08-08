import requests
import uuid
import time
import os

os.system("title NGL Message Sender loop")

print("---------------------------------------------")
print(" NGL Anonymous Message Sender By Unpraised0")
print("---------------------------------------------\n")

username = input("Enter NGL username: ").strip()
message = input("Enter your message: ").strip()

while True:
    try:
        count = int(input("How many times to send: "))
        break
    except ValueError:
        print("❌ Please enter a valid number for count.")

while True:
    try:
        delay = float(input("Delay between each message (seconds): "))
        break
    except ValueError:
        print("❌ Please enter a valid number for delay.")

print(f"\nSending {count} messages to {username} with {delay} seconds delay...\n")

# เริ่มส่งข้อความตามจำนวนรอบ
for i in range(1, count + 1):
    device_id = str(uuid.uuid4())
    print(f"[{i}/{count}] Sending...")

    headers = {
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://ngl.link",
        "referer": f"https://ngl.link/{username}/"
    }

    data = {
        "username": username,
        "question": message,
        "deviceId": device_id,
        "gameSlug": "",
        "referrer": ""
    }

    try:
        response = requests.post("https://ngl.link/api/submit", headers=headers, data=data)
        if response.status_code == 200:
            print(f"✓ Message {i} sent!")
        else:
            print(f"❌ Failed to send message {i}. Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Error: {e}")

    if i < count:
        time.sleep(delay)

print("\nAll messages sent!")
input("Press Enter to exit...")
