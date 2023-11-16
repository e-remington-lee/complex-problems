'''
<, > break the brainscape flash cards for some reason, so we replace them

'''
def file_to_string(file):
    with open(file, "r") as rf:
        lines = rf.read()
        return lines.replace("    ", "----")

        # return lines.replace("    ", "----").replace("<", "[less than]").replace(">", "[greater than]").replace(">=", "[greater than or equal]").replace("<=", "[less than or equal]")

# copy this code into the file, run it, it will print the contents to the console to copy for a flash card
    # import sys
    # sys.path.append(".")
    # from utilities import to_string
    # flashcard=to_string.file_to_string(__file__)
    # print(flashcard)