def exists_word(word, instance):
    file = instance.queue()

    a = [element["linhas_do_arquivo"] for element in file if word == element]
    print("🔥🔥🔥🔥🔥", a)
    # test = [{
    #     "palavra": word,
    #     "arquivo": file["nome_do_arquivo"],
    #     "ocorrencias": [
    #         {
    #         "linha": 2
    #         },
    #         {
    #         "linha": 7
    #         }
    #     ]
    # }]
    return a


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
