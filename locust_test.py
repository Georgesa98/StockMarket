from locust import HttpUser, task
import random
import json


class Transactions(HttpUser):
    @task
    def transact(self):
        random_user = int(random.randint(1, 100))
        random_stock = int(random.randint(1, 6))
        random_quantity = int(random.randint(1, 20))
        random_action = random.choice(["BUY", "SELL"])

        self.client.post(
            "/transactions/",
            json={
                "user": random_user,
                "stock": random_stock,
                "quantity": random_quantity,
                "type": random_action,
            },
        )
