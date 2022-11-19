from .challenges import Challenge_1


def board_formatter(board: str) -> list:
    out = [row.split(" ") for row in board.split("\n")]

    return []


if __name__ == "__main__":
    print(
        board_formatter(
            """\
~ X ~
~ X ~
~ X ~
A ~ B
A ~ B
A ~ B
~ C ~
~ C ~
~ C ~\
"""
        )
    )