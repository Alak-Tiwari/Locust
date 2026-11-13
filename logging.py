#Logging helps to debug your script,CI/CD etc
#Locust uses python's logging framework
#logging.info()
#logging.error()
#logging.critical()
#logging.debug()
#logging.warning()

#cmd for running logging is locust -f filename.py --logfile mylog.log --headless --only-summary
#mylog.log file would be generated after successfull execution of the task 

form locust import HttpUser,SequentialTaskSet,task,constant
import logging 

class PetStore(SequentialTaskSet):
    @task
    def home_page(self):
        with self.client.get("/",catch_response=True,name="Home_Page") as response:
            if "Welcome to JPetStore 6" in response.text:
                response.success()
                logging.info("Home Page load success")#Info is default ,you can change it to debug or anything from 
                #the options available under logging module


            else:
                response.failure("Home Page didn't load successfully.")
                logging.error("Home page didn't load successfully.")

class LoadTest(HttpUser):
    host="https://petstore.octoperf.com"
    wait_time=constant(1)
    tasks=[PetStore]


