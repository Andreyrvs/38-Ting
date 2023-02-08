import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    file = txt_importer(path_file)
    data = {
       "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    for file in range(len(instance)):
        if instance.search(file)["nome_do_arquivo"] == path_file:
            return

    instance.enqueue(data)
    return print(data, file=sys.stdout)

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
