from client import clirequest


def registration(username: str, password: str, password2: str,
                                why_using: str, phone_number: str, region: int, job: int):
    clirequest.register(username, password, password2, phone_number, region, job, why_using)


def auth(username: str, password: str):
    clirequest.authentication(username, password)