import base64
import hashlib
import hmac

from app.dao.user import UserDao
from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import jwt


class UserService:
    def __init__(self, dao: UserDao):
        self.dao = dao
    def get_one(self):
        return self.dao.get_one()
    def get_all(self):
        return self.dao.get_all()
    def create(self, data):
        data["password"] = self.get_hash(data["password"])
        return self.dao.create(data)

    def update(self, data):
        usid = data.get("id")
        user = self.get_one(usid)

        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")
    def delete(self, usid):
        return self.dao.delete(usid)

    def get_by_username(self, username):
        return self.dao.get_by_username(username)

    def get_hash(password):
        return hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ).decode("utf-8", "ignore")

    def compare_password(self, password_hash, other_password):
        decoded_digist = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            "sha256",
            other_password.encode("utf-8"),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digist, hash_digest)