import sys

def txt_importer(path_file):
    if path_file == "":
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    if path_file[len(path_file) - 3] != "txt":
        return print(f"Formato inválido", file=sys.stderr)
    print(f"🌊🌊🌊🌊{path_file}")
    with open(path_file) as file:
        lines = file.readlines()
        for line in lines:
            print(f"{line}\n")
