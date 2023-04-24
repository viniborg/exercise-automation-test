from selenium import webdriver
from selenium.webdriver.remote.remote_connection import RemoteConnection
from src.core.lambda_credentials import LambdaCredentials
from src.utils.json_loader import read_json


class Driver:

    def __init__(self, request):
        self.request = request
        self.driver_instance = self.driver()

    def driver(self):
        desired_capabilities = read_json("src/desired_caps/desired_caps.json")
        options = {
            'name': self.request.node.name,
            **desired_capabilities["browser"],
            'video': desired_capabilities['video'],
            'visual': desired_capabilities['visual'],
            'network': desired_capabilities['network'],
            'console': desired_capabilities['console'],
            'build': desired_capabilities['build'],
        }
        caps = {"LT:Options": options}

        username = LambdaCredentials.get_username()
        access_key = LambdaCredentials.get_access_key()
        lambda_url = f"http://{username}:{access_key}@hub.lambdatest.com/wd/hub"

        executor = RemoteConnection(lambda_url)
        browser = webdriver.Remote(
            command_executor=executor,
            desired_capabilities=caps
        )
        return browser

    def finalize_test(self):
        if self.request.node.rep_call.failed:
            self.driver_instance.execute_script("lambda-status=failed")
        else:
            self.driver_instance.execute_script("lambda-status=passed")
            self.driver_instance.quit()
