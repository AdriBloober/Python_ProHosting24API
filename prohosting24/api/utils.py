from datetime import datetime


class ProHosting24Model:
    def __repr__(self):
        a = f"{type(self).__name__} "
        for k, v in self.__annotations__.items():
            if hasattr(self, k):
                a += k + "=" + str(getattr(self, k)) + " "
        return a


def parse_from_timestamp(timestamp):
    if timestamp is None:
        return None
    else:
        return datetime.fromisoformat(timestamp)


def create_json_object(c, d, *args, **kwargs):
    obj = c(*args, **kwargs)
    for k, v in d.items():
        try:
            if type(v) != str:
                raise ValueError("Argument is not string.")
            setattr(obj, k, parse_from_timestamp(v))
        except ValueError:
            setattr(obj, k, v)
    return obj
