import os
from datetime import datetime
import pytz

def main():

    user_name = os.getenv("USER_NAME", "Guest")

    tz_utc = pytz.utc
    now = datetime.now(tz_utc)

    print("Приветствую, Docker World!")
    print(f"Добро пожаловать, {user_name}!")
    print(f"Current UTC time: {now.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
