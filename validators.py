from exceptions import InvalidArgumentException


def validate_input(payload, requested_params):
    for requested_param in requested_params:
        if not payload.get(requested_param, False):
            raise InvalidArgumentException("you must specify {}".format(requested_param))