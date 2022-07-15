from typing import Dict, List
from database import signs as db_signs


class UserRepo:
    def __init__(self, repo: List) -> None:
        self.repo = repo

    def find(self, id: str) -> Dict | None:
        for user in self.repo:
            if user['id'] == id:
                return user
        return None

    def getAll(self) -> List:
        return self.repo

    def update(self, id: str, name: str, age: int, sign: str) -> Dict | None:
        print(type(id))
        for user in self.repo:
            print(user)
            if user['id'] == int(id):
                user['age'] = age
                user['name'] = name
                user['sign'] = sign
                return user

        return None

    def delete(self, id: str) -> None:
        for user in self.repo:
            if user['id'] == id:
                self.repo.remove(user)
                return user
        return None

    def create(self, name: str, age: str, sign: str) -> Dict | None:
        sign_exist = False

        for db_sign in db_signs:
            if db_sign == sign:
                sign_exist = True

        print(sign_exist)
        if (not sign_exist):
            return None

        print(self.repo[-1]['id'] + 1)

        user = {'id': self.repo[-1]['id'] + 1,
                'name': name, 'age': age, 'sign': sign}
        self.repo.append(user)
        return user
