from os import environ


class LambdaCredentials:
    @staticmethod
    def get_username():
        username = environ.get('LT_USERNAME')
        if not username:
            raise Exception("Could not load variable LT_USERNAME. Check if it is informed in the system variable")
        return username

    @staticmethod
    def get_access_key():
        access_key = environ.get('LT_ACCESS_KEY')
        if not access_key:
            raise Exception("Could not load variable LT_ACCESS_KEY. Check if it is informed in the system variable")
        return access_key
