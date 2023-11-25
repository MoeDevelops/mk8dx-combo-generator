from typing import List


def read_csv(file_path: str) -> List[List[str]]:
    data: List[List[str]] = []

    with open(file_path, "r") as file:
        for line in file:
            splitted_line = line.strip().split(",")
            data.append(splitted_line)

    # remove header
    data.pop(0)

    return data
