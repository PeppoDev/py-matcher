from typing import Dict
import random


class Matcher:
    @staticmethod
    def match(list: str, user: Dict) -> Dict:
        random_index_user = random.randrange(0, len(list) - 1)
        random_percent = random.randrange(50, 100)

        random_user = list[random_index_user]

        if random_user['name'] == user['name']:
            random_percent = 100

        return {"match": random_user, "percent": str(random_percent)+"%"}
