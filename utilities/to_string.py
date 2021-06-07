def file_to_string(file):
    with open(file, "r") as rf:
        lines = rf.read()
        return lines.replace("    ", "----")

    # import sys
    # sys.path.append(".")
    # from utilities import to_string
    # flashcard=to_string.file_to_string(__file__)
    # print(flashcard)