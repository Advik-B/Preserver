import subprocess


INDEX_ID_CMD = ["winget", "list"]
UNTIL_ID_COUNT = 41
HEADER_COUNT = 4


def index_by_id():
    """
    Indexes the apps and returns a list of ids using winget
    NOT RECOMMENDED FOR LARGE AMOUNTS OF APPS
    NOT RELIABLE FOR ALL APPS
    """

    raw_output = subprocess.run(
        INDEX_ID_CMD, stdout=subprocess.PIPE, encoding="utf-8"
    ).stdout

    raw_output_list = raw_output.splitlines()    
    output_list_ = [line[UNTIL_ID_COUNT:] for line in raw_output_list]
    output_list = [line.split(" ")[0] for line in output_list_][HEADER_COUNT:-1]
    output = [
        out
        for out in output_list
        if "{" not in out and "}" not in out and "…" not in out
    ]

    # Free up memory
    del output_list_, raw_output_list, output_list, raw_output
    return output


print(*index_by_id(), sep="\n")
