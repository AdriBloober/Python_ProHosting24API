# Python ProHosting24 API

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
