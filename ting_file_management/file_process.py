import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    """Aqui irá sua implementação"""
    is_duplicate_file = False
    instance_length = instance.__len__()

    for i in range(instance_length):
        searched_dictionary = instance.search(i)
        if path_file == searched_dictionary['nome_do_arquivo']:
            is_duplicate_file = True

    if not is_duplicate_file:
        txt_importation = txt_importer(path_file)

        insert_dictionary = {
                'nome_do_arquivo': path_file,
                'qtd_linhas': len(txt_importation),
                'linhas_do_arquivo': txt_importation
        }

        instance.enqueue(insert_dictionary)
        print(f'{insert_dictionary}', file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""
    instance_length = instance.__len__()

    if instance_length == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        item_dequeue = instance.dequeue()
        path_file = item_dequeue['nome_do_arquivo']
        print(f'Arquivo {path_file} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    try:
        result = instance.search(position)
        print(f'{result}', file=sys.stdout)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
