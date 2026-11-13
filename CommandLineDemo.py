from locust import HttpUser,task,constant
class MyLoadTest(HttpUser):
    wait_time=constant(1)
    @task
    def launch(self):
        self.client.get("/")

# locust -f filename.py -u 1 -r 1 -t 10s --headless --print-stats --csv file.csv --csv-full-history --host=https://ex.com
# locust -f CommandLineDemo.py -u 1 -r 1 -t 5s --headless --print-stats --csv file.csv --csv-full-history --host=https://example.com -L CRITICAL --logfile mylog.log --html Run1
#locust -f CommandLineDemo.py --show-task-ratio-json