# every new 'data' class needs to be included in this import
# and returned its __name__ on the method get_avaiable_classes
# TODO: replace this with something a little more dynamic, trying to import every
# file inside /data/ folder

from data.pessoa import Pessoa

AVAIABLE_CLASSES = {
    'Pessoa' : Pessoa
}

def is_avaiable_class(cls):
    return cls in AVAIABLE_CLASSES

def get_class_from_str(str):
    return AVAIABLE_CLASSES[str]