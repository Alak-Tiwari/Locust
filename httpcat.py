from locust import HttpUser,constant,TaskSet,task
import random

class MyHTTPCat(TaskSet):
    @task
    def get_status(self):
        res=self.client.get("/200")
        print("Get status of 200")

    @task
    def get_random_status(self):
        status_codes=[123, 456, 789, 234, 567, 890, 
        345, 678, 912, 234, 567, 890, 123, 456, 789, 234, 345, 678, 910, 345
        ]
        random_url="/"+str(random.choice(status_codes))
        res=self.client.get(random_url)
        print("Random http status")
        self.interrupt(reschedule=False)

    class MyAnotherHttpCat(TaskSet):
        @task
        def get_500_status(self):
            self.client.get("/500")
            print("Get status of 500")
            self.interrupt(reschedule=False)
            #once the control comes inside the nested class of TaskSet,it never goes out
            #So to break it or to come out to parent class we use self.interrupt(reschedule=True)
            #It will execute it once only and the control would go to parent class
            #But if you want to execute it in equal ratio to the parent class 
            #use self.interrupt(reschedule=False) we will have breath time between the execution of each task or TaskSet

class HttpCat(TaskSet):
    @task
    def meow(self):
        print("Meow")
        self.interrupt(reschedule=False)       
        

class MyLoadTest(HttpUser):
    host="https://http.cat"
    tasks=[MyHTTPCat,HttpCat]
    wait_time=constant(1)