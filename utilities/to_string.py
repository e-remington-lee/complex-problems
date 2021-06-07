def file_to_string(file):
    with open(file, "r") as rf:
        lines = rf.read()
        return lines.replace("    ", "----")

