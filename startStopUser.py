from locust import User,task,constant

class MyTest(User):
    wait_time=constant(1)

    def on_start(self):
        print("Starting")

    @task
    def task_1(self):
        print("Task 1 ")

    def on_stop(self):
        print("Stopping")

#locust -f startStopUser.py -r 1 -u 1 -t 4s --headless --only-summary