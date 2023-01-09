from __future__ import annotations
from dataclasses import dataclass
import csv
import os


def load_challenges() -> list[Challenge]:
    challenges: list[Challenge] = []
    with open("challenges.csv", "r") as file:
        reader = csv.reader(file)
        _ = next(reader)  # Names for each field

        for line in reader:
            challenges.append(Challenge(
                name=line[0],
                location=tuple(line[1].split(" ")),
                target=tuple(line[2].split(" ")),
                instructions=""
            ))

    names = {}
    for instruction_file_name in os.listdir("instructions"):
        with open(instruction_file_name, "r") as instruction_file:
            instructions = instruction_file.readlines()
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
