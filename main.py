import requests
import time
from datetime import datetime

API_URL = "https://wtxmd52.tele68.com/v1/txmd5/lite-sessions?cp=R&cl=R&pf=web&at=d865d79c7e96b7935ac90b36a3748559"

saved_sessions = set()

print("🚀 API RUNNING 24/24")

while True:

    try:

        r = requests.get(API_URL, timeout=10)

        data = r.json()

        sessions = data["list"]

        for s in reversed(sessions):

            session = s["id"]

            if session not in saved_sessions:

                saved_sessions.add(session)

                print({
                    "session": session,
                    "result": s["resultTruyenThong"],
                    "dices": s["dices"],
                    "point": s["point"],
                    "time": datetime.now().strftime("%H:%M:%S")
                })

        # tránh đầy RAM
        if len(saved_sessions) > 50000:
            saved_sessions.clear()

        time.sleep(2)

    except Exception as e:

        print("ERROR:", e)

        time.sleep(5)