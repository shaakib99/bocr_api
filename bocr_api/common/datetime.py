from datetime import datetime, timezone


class DateTime():

    @staticmethod
    def now():
        return datetime.now(timezone.utc).timestamp() * 1000