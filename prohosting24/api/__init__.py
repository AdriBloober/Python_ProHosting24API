from prohosting24.api.endpoints.support_tickets import SupportApi
from prohosting24.api.endpoints.vserver import VServerApi


class Api(VServerApi, SupportApi):
    """All Api parts summarized."""

    pass
