# Python ProHosting24 API

**This is a non-official project!**

## Install

### Install from pip

```
python3 -m pip install --upgrade prohosting24api --user
```

### Manually Installation

```
git clone https://github.com/AdriBloober/Python_ProHosting24API
python3 setup.py install --user
```

## How to use

Open you'r Browser and go to https://prohosting24.de/cp/, the Cookie with name 'ph24_sessionid' contains the SessionID.

```python
from prohosting24 import Api
api = Api("You'r SessionID")
```

### Login

```python
from prohosting24 import Api, login
api = login("youremail@email.com", "TypeInYourPassword")
type(api) == Api
```

If you want to save the api, you must save ``api.sessionid_authentication``.


### Functions with object references

Functions, which begins with a ``@model_target(Model)`` are functions, which requires a object references.
The ``ref`` argument need's a integer id of the Model (in some casese, the model will be requested) or the model.
The Typehints will help you to see the argument types, for example ``Union[VServer, int]``.
If the ``model_target`` has the attribute ``get_model``, the model will be requested if you hand over the integer id.
The ``ref`` attribute has the type ``ModelReference``.

### VServer

VServer Model:
```python
class VServer(ProHosting24Model):
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
```

#### Get a VServer

```python
vserver = api.get_vserver(id_of_vserver)
type(vserver) == VServer
```

#### Start/Stop/Shutdown a VServer

```python
from time import sleep
vserver = api.get_vserver(id_of_vserver)
api.shutdown_server(vserver)
sleep(10)
api.start_server(vserver)
sleep(10)
api.stop_server(vserver) # stop means hard stop (not shutdown)
```

### Support system

Models:
```python
class SupportTicket(ProHosting24Model):
    """Basic informations about a ticket."""
    created_on: datetime
    id: int
    last_answer: int
    serviceid: int
    status: int
    title: str
    userid: int


class SupportAnswer(ProHosting24Model):
    """A answer to a ticket."""
    created_on: datetime
    extern: int
    id: int
    mitarbeiter: int
    vorname: str
    nachname: str
    text: str
    userid: int


class InspectedSupportTicket(SupportTicket):
    """A support ticket with informations and answers."""
    answers: List[SupportAnswer] = []
```

#### Get own support tickets

```python
tickets = api.get_own_support_tickets()
type(tickets) == List[SupportTicket]
```

#### Inspect support ticket

```python
ticket = api.inspect_support_ticket(ticket_id)
type(ticket) == InspectedSupportTicket
```
