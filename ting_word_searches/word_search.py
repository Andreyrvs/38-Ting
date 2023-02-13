
def exists_word(word, instance):
    find_word = list()
    word_lower = word.lower()

    for file_index in range(len(instance)):
        file = instance.search(file_index)
        print('file: ', file)

        data = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": list(),
        }

    return find_word

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
