import pickle
import os
import uuid
from exceptions import InvalidIdException


def get_target(destiny):
    return "./fake_db/" + destiny


def save(destiny, obj):
    target = get_target(destiny)
    list_objects = []
    if os.path.getsize(target) > 0:
        with open(target, "rb") as dest_file:
            list_objects = pickle.load(dest_file)

    obj.update({"id": str(uuid.uuid4())})
    list_objects.append(obj)
    with open(target, "wb") as dest_file:
        pickle.dump(list_objects, dest_file)
    return {"object_id": obj["id"]}


def get(destiny):
    with open(get_target(destiny), "rb") as dest_file:
        return pickle.load(dest_file)


def get_by_id(destiny, object_id):
    table = get(destiny)
    for row in table:
        if row["id"] == object_id:
            return row

    raise InvalidIdException("Invalid ObjectId provided")


def update(destiny, object_id, updated_obj):
    table = get(destiny)
    for row in table:
        if row["id"] == object_id:
            row.update(updated_obj)

    with open(get_target(destiny), "wb") as dest_file:
        pickle.dump(table, dest_file)
