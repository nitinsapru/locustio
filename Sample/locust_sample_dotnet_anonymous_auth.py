#importing necessary dependencies from locust library#
from locust import HttpLocust, TaskSet, task

#class which hosts multiple method definitions to undertake different type of user activities#
class UserBehavior(TaskSet):

#using decorator @task over the index method which will invoke a HTTP client to hit the root site#
    @task(2)
    def index(self):
        self.client.get("/")

#using decorator @task over the contact method which will invoke a HTTP client to hit the /home/contact site#
    @task(1)
    def contact(self):
        self.client.get("/home/contact")

#using decorator @task over the about method which will invoke a HTTP client to hit the /home/about site#
    @task(1)
    def about(self):
        self.client.get("/home/about")

#using decorator @task over the apirestmethod1 method which will invoke a HTTP client to hit the /api/apirestmethod1 site#
    @task(1)
    def apirestmethod1(self):
        self.client.get("/api/RestEndpoint1")

    @task(1)
    def apirestmethod2(self):
        self.client.get("/api/RestEndpoint2")

#class which defines the min wait time for request & max wait time before subsequent requests & takes in HTTP site URL for load testing#
class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 10000
    max_wait = 19000