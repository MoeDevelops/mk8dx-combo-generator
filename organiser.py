def organize_data(file_path_read: str, file_path_write: str):
    new_file = []

    with open(file_path_read, "r") as file:
        # copy header
        new_file.append(file.readline())

        for line in file:
            split_values = line.split(",", 1)
            name = split_values[0]
            stats = split_values[1]

            stats_found = False

            for new_line in new_file:
                if stats in new_line:
                    index = new_file.index(new_line)
                    new_file[index] = name + " | " + new_line
                    stats_found = True
                    break

            if not stats_found:
                new_file.append(line)

    with open(file_path_write, "w") as file:
        file.writelines(new_file)


file_parts = ["bodies", "drivers", "gliders", "tires"]

for file_part in file_parts:
    organize_data(f"data/{file_part}.all.csv", f"data/{file_part}.csv")
