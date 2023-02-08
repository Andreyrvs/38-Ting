import sys

def txt_importer(path_file):
    print('path_file: ', path_file)
    if path_file == "":
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)

    if path_file[len(path_file) - 4] != ".txt":
        return print(f"Formato inválido", file=sys.stderr)

    with open(path_file) as file:
        lines = file.readlines()
        for line in lines:
            return f"{line}\n"
