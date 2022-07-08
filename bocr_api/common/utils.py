import json
from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet
from uuid import uuid4
import hashlib

load_dotenv()


class Utils():
    __encode_type = "utf8"
    __key = os.getenv("SECRET_KEY").encode(__encode_type)
    __fernet = Fernet(__key)

    @staticmethod
    def generate_random_uuid():
        return uuid4().hex

    def encrypt(self, payload: dict):
        return self.__fernet.encrypt(
            json.dumps(payload).encode(self.__encode_type)).decode(
                self.__encode_type)

    def decrypt(self, token: str):
        return json.loads(
            self.__fernet.decrypt(token.encode(self.__encode_type)))

    def hash_password(self, password: str):
        return hashlib.sha512(
            password.encode(self.__encode_type) + self.__key).hexdigest()
