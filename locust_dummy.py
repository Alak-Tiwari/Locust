#correlation
#At each request new token is generated so one need to dynamically capture at every request
#so for that purpose token is used
#capturing the value and storing its value in variable and sending it with request
from locust import HttpUser,SequentialTaskSet,task,constant
import random
import re #re stands for regular expression(importing regular expression module)

class PetStore(SequentialTaskSet):
    def __init__(self, parent): 
        super().__init__(parent)
        self.jsession=""
        self.random_product=""

    @task
    def home_page(self):
        with self.client.get("",catch_response=True,name="TOO_Homepage") as response:
            if "Welcome to JPetStore 6" in response.text and response.elapsed.total_seconds()<2.0:
                response.success()
            else:
                response.failure("Home page took too long to load and/or text check has failed.")

    @task
    def enter_store(self):
        products=['Fish','Dogs','Cats','Reptiles','Birds']
        with self.client.get("/actions/Catalog.action",catch_response=True,name="T10_EnterStore") as response:
            print(response.text)
            for product in products:
                if product  in response.text:
                    response.success()
                else:
                    response.failure("Products check failed")
                    break
            
            try:
                jsession=re.search(r"jsessionid=(.+?)\?",response.text)
                self.jsession=jsession.group(1)# type: ignore #here group(1) means it will search for the first jsession if more than one jsession are present

            except AttributeError:
                self.jsession=""


    @task
    def signin_page(self):
        self.client.cookies.clear()
        url="/actions/Account.action;jsessionid="+self.jsession+"?signonForm="
        with self.client.get(url,catch_response=True,name="Sign-inPage") as response:
            if "Please enter your username and password." in response.text:
                response.success()
            else:
                response.failure("Sign in failed")

    @task
    def login(self):
        self.client.cookies.clear()
        url="/actions/Account.action"
        data={
            "username":"j2ee",
            "password":"j2ee",
            "signon":"Login"
        }
        with self.client.post(url,catch_response=True,data=data,name="SignInLandingPage") as response:
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    random_product=re.findall(r"")
