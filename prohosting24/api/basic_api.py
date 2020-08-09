import requests

from prohosting24.api.error_mangement import handle_response


class BasicApi:
    """The Basic API with request handlers, authentication and api_path."""

    def handle_request(self, method, function, data, headers=None, **kwargs):
        if headers is None:
            headers = {}
        data["sessionid"] = self.sessionid_authentication
        headers["function"] = function
        response = requests.request(
            method.lower(), self.api_path, data=data, headers=headers, **kwargs
        )
        return handle_response(response)

    def __init__(
        self, sessionid_authentication, api_path="https://intern.api.prohosting24.de"
    ):
        """
        :param sessionid_authentication: The sessionid for authentication. You can find the sessionid in the cookies
        of your  browser.
        :param api_path: The path to the api.
        """
        self.sessionid_authentication = sessionid_authentication
        self.api_path = api_path
