from locust import HttpUser, constant, task

class MyReqRes(HttpUser):
    host = "https://reqres.in"  # Define the base URL for the requests also you can send host in command line : locust -f reqres.py --host=https://reqres.in
    wait_time = constant(1)  # Define the wait time between tasks (1 second)

    @task
    def get_users(self):
        # Simulate a GET request to fetch users
        res=self.client.get("/api/users?page=2")
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_user(self):
        # Simulate a POST request to create a user
        res=self.client.post("/api/users", data='''{"name": "morpheus", "job": "leader"}''')
        print(res.text)
        print(res.status_code)
        print(res.headers)