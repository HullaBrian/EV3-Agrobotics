from __future__ import annotations
from dataclasses import dataclass
import csv
import os


def load_challenges() -> list[Challenge]:
    challenges: list[Challenge] = []
    with open(os.path.join(os.getcwd(), "challenges", "challenges.csv"), "r") as file:
        reader = csv.reader(file)
        _ = next(reader)  # Names for each field

        for line in reader:
            challenges.append(Challenge(
                name=line[0],
                location=tuple(int(i) for i in line[1].split(" ")),
                target=tuple(int(i) for i in line[2].split(" ")),
                instructions=""
            ))

    names = {}
    for instruction_file_name in os.listdir(os.path.join(os.getcwd(), "challenges", "instructions")):
        with open(os.path.join(os.getcwd(), "challenges", "instructions", instruction_file_name), "r") as instruction_file:
            instructions = "\n".join(instruction_file.readlines())
        names[instruction_file_name.replace(".txt", "")] = instructions

    for challenge in challenges:
        challenge.instructions = names[challenge.name]

    return challenges


@dataclass
class Challenge:
    name: str
    location: tuple
    target: tuple
    instructions: str
