"""
    Módulo para justificar texto en archivos de .txt o .doc

"""

from typing import List, Dict


def longest_common_substring(string1: str, string2: str) -> int:
    """ 
    Dados dos strings retorna el largo del substring más largo en común
    Ej: longest_common_substring('abcdxyz', 'zyxabcd') = 4

    Inputs:
    -------
    string1, string2: str
        Strings a comparar y buscarles el substring más largo en común

    Output:
    -------
    int:
        Largo del substring en común más largo
    """
    ...


def word_break(input_str: str, word_list: List[str]) -> bool:
    """
    Dados un string y una lista de palabras, se verifica si el input
    puede escribirse como una secuencia de palabras de la lista
    Ej: word_break('holamundo', ['hola', 'mundo', 'python']) = True

    Inputs:
    -------
    input_str: str
        String a separar
    word_list: List[str]
        Lista de palabras disponibles

    Output:
    -------
    bool:
        True si la palabra se puede escribir como secuencia, False si no
    """
    # Caso base: palabra vacía, trivialmente divisible como secuencia
    if input_str == '':
        return True
    # revisamos cada parte del string por caracter
    for i in range(1, len(input_str)+1):
        word_found = input_str[:i] in word_list
        # si en los primeros i caracteres no hay una palabra, se continua
        if not word_found:
            continue
        # si se encuentra una palabra, se verifica recursivamente que el resto
        # del string sea divisible en una secuencia
        if word_break(input_str[i:], word_list):
            return True
    # si no se logra la división, se retorna False
    return False


def word_wrap(
        word_lengths: List[int],
        total_words: int,
        actual_word: int,
        max_lin_width: int,
        remaining_space: int,
        cost_matrix: List[List[int]]
    ):
    ...



if __name__ == '__main__':
    dictionary = [
        'i', 
        'like', 
        'sam',
        'sung',
        'samsung', 
        'mobile', 
        'ice', 
        'cream', 
        'icecream', 
        'man', 
        'go', 
        'mango',
    ]
    print(word_break('ilikesamgo', dictionary))