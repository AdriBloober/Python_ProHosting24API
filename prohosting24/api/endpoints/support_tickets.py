from datetime import datetime

from typing import List

from prohosting24.api.basic_api import BasicApi
from prohosting24.api.utils import create_json_object, ProHosting24Model


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


class SupportApi(BasicApi):
    def get_own_support_tickets(self) -> List[SupportTicket]:
        """
        :return: A list of SupportTickets (Basic informations without answers)
        """
        return [
            create_json_object(SupportTicket, element)
            for element in self.handle_request("POST", "getownsupporttickets", {})
        ]

    def inspect_support_ticket(self, ticket_id) -> InspectedSupportTicket:
        """
        :param ticket_id: The id of the inspecting ticket.
        :return: A InspectedSupportTicket object with basic informations and answers.
        """
        j = self.handle_request("POST", "supportticketdetails", {"ticketid": ticket_id})
        c = create_json_object(InspectedSupportTicket, j["0"])
        [
            c.answers.append(create_json_object(SupportAnswer, answer))
            for answer in j["answer"]
        ]
        return c
