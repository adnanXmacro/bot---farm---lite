import time, os, random

class Bot:
    def __init__(self):
        self.username = os.getenv("BOT_USERNAME", "default_bot")
        self.targets = os.getenv("TARGET_USERS", "elonmusk,oprah").split(",")

    def login(self):
        print(f"[{self.username}] Logged in ✅")

    def follow(self, user):
        print(f"[{self.username}] Following {user} 💥")
        time.sleep(random.uniform(1.5, 3.0))  # Fake human delay

    def run(self):
        self.login()
        for user in self.targets:
            self.follow(user)
        print(f"[{self.username}] Done.")
