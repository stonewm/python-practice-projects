import json
import tablib

def to_formatted_table(tab_data):
    """
    tab_data is supposed to be of type list(dict)
    """
    ds = tablib.Dataset()
    return(ds.load(str(tab_data)))


class ModelExt(object):
    """
    Model extension, implementing `__repr__` method which returns all the class attributes
    """
    def __repr__(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]

        return json.dumps(fields)