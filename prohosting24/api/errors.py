class ProHosting24Error(Exception):
    pass


class AccessDeniedKVMServer(ProHosting24Error):
    pass


class AccessDeniedTicket(ProHosting24Error):
    pass


class InvalidSessionID(ProHosting24Error):
    pass


class MissingVariableInPOST(ProHosting24Error):
    pass


class InvalidCredentials(ProHosting24Error):
    pass


exceptions = {
    "Nicht Ihr KVM Server": AccessDeniedKVMServer,
    "Dieses Ticket gehört einem anderem Nutzer": AccessDeniedTicket,
    "Keine Valide SessionId.": InvalidSessionID,
    "Missing Variable in POST": MissingVariableInPOST,
    "Sie haben falsche Anmeldeinformationen angegeben.": InvalidCredentials,
}
