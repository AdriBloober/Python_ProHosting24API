from typing import Union

from prohosting24.api.basic_api import BasicApi
from datetime import datetime

from prohosting24.api.utils import create_json_object, ProHosting24Model, model_target


class VServer(ProHosting24Model):
    """The VServer Model with all attributes."""

    expire_at: datetime
    delete_at: datetime
    serviceid: int
    status: str
    id: int
    nodeid: int
    userid: int
    cores: int
    memory: int
    disk: int
    proxmoxid: str
    backupslots: int
    backuphour: int
    packet: int
    imageid: int
    price: float
    discount: str
    created_on: datetime
    ip: int
    daysleft: int
    uptime: int
    timeleft: int


class VServerApi(BasicApi):
    def get_vserver(self, vserver_id) -> VServer:
        """Get informations about a VServer by his id.
        :param vserver_id: The id of the vserver.
        :return A `class`:VServer Object.
        """
        return create_json_object(
            VServer, self.handle_request("POST", "getvserverinfos", {"id": vserver_id})
        )

    @model_target(VServer)
    def shutdown_server(self, ref: Union[VServer, int]):
        self.handle_request("POST", "vservershutdown", {"id": ref.id})

    @model_target(VServer)
    def start_server(self, ref: Union[VServer, int]):
        self.handle_request("POST", "vserverstart", {"id": ref.id})

    @model_target(VServer)
    def stop_server(self, ref: Union[VServer, int]):
        self.handle_request("POST", "vserverstop", {"id": ref.id})
