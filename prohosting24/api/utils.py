from datetime import datetime
import inspect


class ProHosting24Model:
    def __repr__(self):
        a = f"<{type(self).__name__} "
        for k, v in self.__annotations__.items():
            if hasattr(self, k):
                a += k + "=" + str(getattr(self, k)) + " "
        return a + ">"


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


class ModelReference:
    def __init__(self, id: int, model=None):
        self.id = id
        self.model = model

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id} model={self.model}>"


def model_target(model_class, get_model=None, getmodel_args=None):
    if not getmodel_args:
        getmodel_args = ()
    if type(getmodel_args) == list:
        getmodel_args = tuple(getmodel_args)

    def run(f):
        target_arg_key = None
        l = list(inspect.signature(f).parameters.keys())
        for i in range(len(l)):
            c = l[i]
            if c.lower().startswith("ref"):
                target_arg_key = i
                break

        def k(*args, **kwargs):
            target = args[target_arg_key]
            args = list(args)
            if type(target) == model_class:
                args[target_arg_key] = ModelReference(target.id, target)
                f(*tuple(args), **kwargs)
            elif get_model is None:
                args[target_arg_key] = ModelReference(target)
                f(*tuple(args), **kwargs)
            else:
                get_model_inspect = list(inspect.signature(get_model).parameters.keys())
                get_model_args = []
                if get_model_inspect[0] == "self" and l[0] == "self":
                    get_model_args.append(args[0])
                get_model_args.append(target)
                get_model_args.extend(list(getmodel_args))
                target = get_model(*tuple(get_model_args))
                args[target_arg_key] = ModelReference(target.id, target)
                f(*tuple(args), **kwargs)

        return k

    return run
