from __future__ import annotations
from dataclasses import dataclass
import csv
import os
import re


def get_trailing_number(s) -> int:
    m = re.search(r'\d+$', s)
    return int(m.group()) if m else None


def load_challenges() -> list[Challenge]:
    challenges: list[Challenge] = []
    with open(os.path.join(os.getcwd(), "challenges", "challenges.csv"), "r") as file:
        reader = csv.reader(file)
        _ = next(reader)  # Names for each field

        lines = []
        for index, line in enumerate(reader):
            challenges.append(Challenge(
                name=line[0],
                location=tuple(int(i) for i in line[1].split(" ")),
                target=tuple(int(i) for i in line[2].split(" ")),
                instructions=""
            ))
            lines.append(line)

    names = {}
    for instruction_file_name in os.listdir(os.path.join(os.getcwd(), "challenges", "instructions")):
        with open(os.path.join(os.getcwd(), "challenges", "instructions", instruction_file_name), "r") as instruction_file:
            instructions = "\n".join(instruction_file.readlines())
        names[instruction_file_name.replace(".txt", "")] = instructions

    for challenge in challenges:
        challenge.instructions = names[challenge.name]

    for index, challenge in enumerate(challenges[1:]):
        tmp = challenges[index - 1].name
        if tmp == challenge.name:
            trail = get_trailing_number(tmp)
            if trail is not None:
                challenge.name += str(trail + 1)
            else:
                challenge.name += "-1"

    print(challenges)
    return challenges


@dataclass
class Challenge:
    name: str
    location: tuple
    target: tuple
    instructions: str
