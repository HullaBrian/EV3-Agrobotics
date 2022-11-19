# DO NOT RUN ON EV3


class Challenge(object):
    """
    Challenge parent object
    """
    def __init__(self, name: str = None, position: tuple[int, int] = (-1. -1)):
        self.name: str = name
        self.position: tuple[int, int] = position

    def run(self) -> bool:
        """
        Used by children to implement instructions for the challenge
        """
        raise RuntimeError(f"Challenge {self.name} doesn't have it's run() method initialized!")