import os

class loadenv():
    def __init__(self) -> None:
        self.port = os.getenv("PORT")
        self.username = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.server = os.getenv("SERVER")
        self.school = os.getenv("SCHOOL")
        self.useragent = os.getenv("USER_AGENT")
