from locust import HttpUser,constant,task,SequentialTaskSet
from readTestData import CsvRead

class MyScript(SequentialTaskSet):
    @task
    def place_order(self):
        test_data=CsvRead("cust-data.csv").read()
        print(test_data)

        data={
            "custname":test_data['name'],
            "custtel":test_data['phone_number'],
            "custemail":test_data['email'],
            "size":test_data['size'],
            "topping":test_data['topping'],
            "delivery":test_data['time'],
            "comments":test_data['special_request']
        }

        name='order for'+test_data['name']

        with self.client.post("/post",catch_response=True,name=name,data=data) as response:
            if response.status_code==200 and test_data['name'] in response.text:
                response.success()
            else:
                response.failure("Failure in processing the order")

class MyLoadTest(HttpUser):

    host="https://httpbin.org"
    wait_time=constant(1)
    tasks=[MyScript]