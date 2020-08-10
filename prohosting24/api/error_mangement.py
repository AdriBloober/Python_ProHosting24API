import logging

from prohosting24.api.errors import exceptions, ProHosting24Error


def get_error_by_name(name):
    error = exceptions.get(name, ProHosting24Error)
    if error == ProHosting24Error:
        logging.error(f"Unknown error occured: '{name}'")
        raise error(f"Unknown error: '{name}'")
    raise error(name)


def handle_response(response):
    response.raise_for_status()
    j = response.json()
    if "fail" in j and "error" in j and j["fail"]:
        logging.info(f"E: {j['error']}")
        get_error_by_name(j["error"])
    elif "response" not in j:
        return None

    return response.json()["response"]
