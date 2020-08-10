from prohosting24.api.endpoints.support_tickets import SupportApi
from prohosting24.api.endpoints.vserver import VServerApi


class Api(VServerApi, SupportApi):
    """All Api parts summarized."""

    pass


def login(email, password, api_path="https://intern.api.prohosting24.de") -> Api:
    api = Api(None, api_path)
    api.sessionid_authentication = api.handle_request(
        "POST",
        "login",
        {"email": email, "password": password, "length": 10},
        authentication=False,
    )
    return api
