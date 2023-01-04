class challenge(object):
    """
    This is the parent class for all classes/modules in the challenges directory.
    Peta' Griffin
    """

    def __init__(self, location: tuple, direction: tuple | str):
        self.location = location
        self.direction = direction  # direction represents either a direction vector or a str containing "ANY"
