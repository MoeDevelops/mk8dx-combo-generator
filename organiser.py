import os


file_parts = ["bodies", "drivers", "gliders", "tires"]


def main(standard_config: bool = True):
    ignore_invincibility = False

    if not standard_config:
        ignore_invincibility = input("Ignore invincibility? (y) ") == "y"

    for file_part in file_parts:
        organize_data(f"data/{file_part}.all.csv",
                      f"data/{file_part}.csv",
                      ignore_invincibility)


def organize_data(file_path_read: str, file_path_write: str, ignore_invincibility: bool):
    if os.path.exists(file_path_write):
        os.remove(file_path_write)

    new_file = []

    with open(file_path_read, "r") as file:
        # copy header
        new_file.append(file.readline())

        for line in file:
            split_values = line.split(",", 1)
            name = split_values[0]
            stats = split_values[1]

            if ignore_invincibility:
                split_stats = stats.split(',')
                index = 12
                split_stats[index] = "0" + split_stats[index][1:]
                stats = ",".join(split_stats)

            stats_found = False

            for new_line in new_file:
                if stats in new_line:
                    index = new_file.index(new_line)
                    new_file[index] = name + " | " + new_line
                    stats_found = True
                    break

            if not stats_found:
                new_file.append(name + "," + stats)

    with open(file_path_write, "w") as file:
        file.writelines(new_file)


def files_exist():
    for file_part in file_parts:
        if os.path.exists(f"data/{file_part}.csv"):
            return True

    return False


if __name__ == "__main__":
    main(False)
