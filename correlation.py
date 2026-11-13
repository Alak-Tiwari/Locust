from locust import HttpUser, SequentialTaskSet, task, constant
import re
import random
import logging

# Setting up logging to see logs in terminal
logging.basicConfig(level=logging.INFO)

class PetStore(SequentialTaskSet):

    def __init__(self, parent):
        super().__init__(parent)
        self.jsession = ""
        self.random_product = ""

    @task
    def home_page(self):
        with self.client.get("", catch_response=True, name="T00_HomePage") as response:
            if "Welcome to JPetStore 6" in response.text:
                response.success()
            else:
                response.failure("Home page took too long to load and/or text check has failed.")

    @task
    def enter_store(self):
        products = ['Fish', 'Dogs', 'Cats', 'Reptiles', 'Birds']
        with self.client.get("/actions/Catalog.action", catch_response=True, name="T10_EnterStore") as response:
            for product in products:
                if product in response.text:
                    response.success()
                else:
                    response.failure("Products check failed.")
                    break
            try:
                jsession = re.search(r"jsessionid=(.+?)\?", response.text)  # Extracting the jsession id
                if jsession:
                    self.jsession = jsession.group(1)
            except AttributeError:
                self.jsession = ""

    @task
    def signin_page(self):
        if self.jsession:  # Check if jsession is valid before making the request
            self.client.cookies.clear()
            url = f"/actions/Account.action;jsessionid={self.jsession}?signonForm="
            with self.client.get(url, catch_response=True, name="T20_SignInPage") as response:
                if "Please enter your username and password." in response.text:
                    response.success()
                else:
                    response.failure("Sign in page check failed")
        else:
            logging.warning("No jsession found, skipping signin_page.")

    @task
    def login(self):
        self.client.cookies.clear()
        url = "/actions/Account.action"
        data = {
            "username": "j2ee",
            "password": "j2ee",
            "signon": "Login"
        }
        with self.client.post(url, name="T30_SignIn", data=data, catch_response=True) as response:
            if "Welcome ABC!" in response.text:
                response.success()
                try:
                    random_product = re.findall(r"Catalog.action\?viewCategory=&categoryId=(.+?)\"", response.text)  # Extracting all the products
                    if random_product:
                        self.random_product = random.choice(random_product)  # Storing the random product
                    else:
                        self.random_product = ""
                except AttributeError:
                    self.random_product = ""
            else:
                response.failure("Sign in Failed")

    @task
    def random_product_page(self):
        if self.random_product:  # Ensure random_product is set before proceeding
            url = f"/actions/Catalog.action?viewCategory=&categoryId={self.random_product}"
            name = f"T40_{self.random_product}_Page"
            with self.client.get(url, name=name, catch_response=True) as response:
                if self.random_product in response.text:
                    response.success()
                else:
                    response.failure("Product page not loaded")
        else:
            logging.warning("Random product not set, skipping product page.")

    @task
    def sign_out(self):
        with self.client.get("/actions/Account.action?signoff=", name="T50_SignOff", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Log off failed")
        self.client.cookies.clear()


class LoadTest(HttpUser):
    host = "https://petstore.octoperf.com"
    wait_time = constant(1)
    tasks = [PetStore]
