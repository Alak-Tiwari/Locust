from locust import User,task,constant,between,constant_Pacing

class MyUser(User):
    #constant_pacing(5) no matter what it will wait for 5 seconds
    wait_time=constant(1)
    @task
    def launch(self):
        print("This will inject 1 second delay")
        
