import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    file_txt = txt_importer(path_file)
    data = {
       "nome_do_arquivo": path_file,
        "qtd_linhas": len(file_txt),
        "linhas_do_arquivo": file_txt,
    }

    instance.enqueue(data)
    return print(data, file=sys.stdout)

def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
