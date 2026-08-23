from datetime import datetime


LOG_FILE = "log.txt"


def log_error(message):
    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now()} | ERROR | {message}\n")