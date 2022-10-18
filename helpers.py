import pickle
import os


def get_target(destiny):
    return "./fake_db/" + destiny


def save(destiny, obj):
    target = get_target(destiny)
    list_objects = []
    if os.path.getsize(target) > 0:
        with open(target, "rb") as dest_file:
            list_objects = pickle.load(dest_file)

    list_objects.append(obj)
    with open(target, "wb") as dest_file:
        pickle.dump(list_objects, dest_file)
        

def get(destiny):
    with open(get_target(destiny), "rb") as dest_file:
        return pickle.load(dest_file)