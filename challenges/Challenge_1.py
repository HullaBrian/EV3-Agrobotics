from challenges import Challenge


class Challenge_1(Challenge):
    def __init__(self, position: tuple[int, int]= (-1, -1)):
        super().__init__("1", position)

    def run(self) -> bool:

        return False