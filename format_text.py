from typing import Dict, List


def file_to_str(path: str) -> str:
    """
    Función que lee un archivo .txt y devuelve el texto separado por espacios
    """
    with open(path, 'r') as file:
        return file.read().replace('\n', ' ')


def justify_line(line: str, max_width: int) -> str:
    """
    Función que llena una línea con espacios hasta alcanzar el máximo

    Inputs:
    -------
    line: str
        Línea que se quiere justificar
    max_width: int
        Máximo tamaño de la línea

    Output:
    -------
    str:
        Línea justificada hasta el máximo 
    """
    # si la línea ya ocupa el máximo, se termina
    if len(line) == max_width:
        return line
    words = line.split(' ')
    # si solo hay una palabra, también se termina
    # porque no hay espacios extra que agregar
    if len(words) == 1:
        return line
    # se calcula el espacio extra restante y su distribución
    # entre las palabras
    free_space = max_width - len(line)
    n_spaces = len(words) - 1
    extra_space = free_space % n_spaces
    space_width = (free_space // n_spaces) + 1
    # si es divisible perfectamente, solo se reparten los espacios
    if extra_space == 0:
        return (space_width*' ').join(words)
    # si no lo es, los espacios extra que quedan se reparten desde el inicio
    output_text = ''
    for i in range(n_spaces):
        # cuando se acaba el espacio extra, se termina
        if not extra_space:
            end_of_line = (space_width*' ').join(words[i:])
            return output_text + end_of_line
        # si queda espacio, se agrega uno a cada espacio entre
        # las palabras desde el inicio
        output_text += words[i] + (space_width + 1)*' '
        extra_space -= 1
    

def text_to_file(text: List[str], path: str) -> None:
    """
    Función que guarda un texto por líneas en un archivo .txt
    """
    with open(path, 'w')as file:
        for line in text:
            file.write(line + '\n')


def word_wrap(words: List[str], max_width: int) -> List[str]:
    """
    Función que toma palabras y las distribuye en líneas de manera óptima

    Inputs:
    -------
    words: List[str]
        Lista de palabras a distribuir
    max_width: int
        Tamaño máximo de cada línea
    
    Output:
    -------
    List[str]:
        Texto óptimamente separado por líneas
    """
    n = len(words)
    lengths = [len(word) for word in words]

    costs_list = {}  # lista de costos para programación dinámica
    breaks = {}  # seguimiento de los salto de línea óptimos
    # se calcula recursivamente la mejor distribución del texto
    cost = word_minimal_cost(lengths, max_width, n, 0, costs_list, breaks)
    print(f"Costo del texto: {cost}")
    # se recupera el texto separado en líneas según la función anterior
    lines = []
    i = 0
    while i < n:
        j = breaks[i]
        line = ' '.join(words[i:j])
        lines.append(line)
        i = j
    return lines

def word_minimal_cost(
    lengths: List[int], 
    max_width: int,
    n: int, 
    i: int, 
    costs_list: Dict[int, int], 
    breaks: Dict[int, int]
    ) -> int:
    """
    Función que calcula el menor costo de la i-ésima palabra

    Inputs:
    -------
    lengths: List[int]
        Largos de cada palabra del texto<
    max_width: int
        Largo máximo de cada línea
    n: int
        Total de palabras
    i: int
        Palabra a la cual se le calcula el menor costo
    costs_list: Dict[int, int]
        Lista de costos para cada palabra
    breaks: Dict[int, int]
        Lista de las separaciones óptimas para cada línea

    Output:
    -------
    int: 
        Menor costo de la i-ésima palabra
    """
    # Caso base: se llega a la última palabra
    if i == n:
        return 0
    # si el costo ya se calculó, se devuelve
    if i in costs_list:
        return costs_list[i]
    # si no, se inicializan las variables
    min_cost = float('inf')  # costo inicial infinito
    current_length = 0  # largo de la línea = 0
    best_break = i  # mejor corte es la palabra actual

    # se intenta poner desde la i-ésima a la j-ésima palabra en una línea
    for j in range(i, n):
        current_length += lengths[j]

        # si se supera el largo, entonces no puede seguir aumentando la línea
        if current_length > max_width:
            break
        # se calcula el costo actual de la línea
        remaining_spaces = max_width - current_length
        current_cost = remaining_spaces ** 2

        # se calcula el costo desde la palabra siguiente
        next_cost = word_minimal_cost(lengths, max_width, n, j+1, costs_list, breaks)
        # el costo total va a ser el costo de la línea sumado al costo de las siguientes
        total_cost = current_cost + next_cost

        # se actualiza el menor costo y el mejor quiebre
        if total_cost < min_cost:
            min_cost = total_cost
            best_break = j + 1

        current_length += 1  # se considera el espacio entre la línea y la palabra siguiente

    # se guardan los resultados en las listas para optimizar el código
    # y para hacer seguimiento de los mejores quiebres de línea
    costs_list[i] = min_cost
    breaks[i] = best_break
    return costs_list[i]


def format_text(input_text: str, max_width: int) -> List[str]:
    """
    Formatea un texto en líneas de un largo máximo

    Inputs:
    -------
    input_text: str
        Texto a formatear
    max_width: int
        largo máximo de cada línea

    Output:
    -------
    List[str]:
        Texto formateado por líneas
    """
    # se separa el texto por palabra
    words = input_text.split(' ')
    print(f"Número de palabras: {len(words)}")
    print(f"Largo máximo: {max_width}")
    # se encuentra la separación óptima del texto
    lines = word_wrap(words, max_width)
    # se justifica el texto agregando espacios a cada línea
    # hasta llenar el máximo
    return [justify_line(line, max_width) for line in lines]
