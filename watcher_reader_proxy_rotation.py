
from telethon.sync import TelegramClient
from telethon import connection
import logging
import time

logging.basicConfig(level=logging.INFO)

api_id = 21120428
api_hash = '271c0da5ef59b2a475b7a64e69388e4e'
session_name = 'watcherguru_session_rotating'

# Danh sách proxy SOCKS (IP, Port)
proxy_list = [
    ('47.250.155.254', 80),
    ('185.199.229.156', 7492),
    ('185.199.228.123', 7300),
    ('51.83.79.229', 19050),
    ('103.162.205.131', 4145)
]

def test_and_connect():
    for proxy in proxy_list:
        try:
            print(f"🚀 Đang thử proxy {proxy[0]}:{proxy[1]} ...")
            with TelegramClient(session_name, api_id, api_hash, proxy=proxy,
                                connection=connection.tcp.ConnectionTcp) as client:
                messages = list(client.iter_messages('@WatcherGuru', limit=1))
                if messages:
                    print("✅ Kết nối thành công! Tin mới nhất:")
                    print(f"[{messages[0].date}] {messages[0].text}")
                    return
        except Exception as e:
            print(f"❌ Proxy {proxy} thất bại: {e}")
            time.sleep(1)
    print("❌ Không proxy nào hoạt động được. Vui lòng thử lại sau hoặc đổi mạng/VPN.")

import time

if __name__ == '__main__':
    while True:
        fetch_latest_messages(limit=1)
        print("⏳ Đợi 5 phút trước lần lấy tiếp theo...\n")
        time.sleep(300)  # 5 phút

