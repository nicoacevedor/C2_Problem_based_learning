"""
    Módulo para justificar texto en archivos de .txt o .doc

"""

from argparse import ArgumentParser
from pathlib import Path
from format_text import format_text, file_to_str, text_to_file


def create_parser() -> ArgumentParser:
    """
    Crea un objeto ArgumentParser para llamar al programa
    con argumentos en la línea de comandos
    """
    parser = ArgumentParser()
    parser.add_argument('filepath', type=str)
    parser.add_argument('max_width', type=int)
    parser.add_argument('--sobreescribir', '-s', action='store_true')
    return parser


def main(path: str, max_width: int, overwrite: bool) -> None:
    """
    Recibe el path de un archivo de texto y lo formatea para
    justificar el texto

    Input:
    ------
    path: str
        Path al archivo a modificar
    """
    # lectura del archivo
    text = file_to_str(str(path))
    print('Formateando...')
    # formateo del texto usando el módulo format_text.py
    formated_text = format_text(text, max_width)
    # si no se sobreescribe el archivo, se crea uno nuevo
    if not overwrite:
        new_path = Path(path)
        path = str(new_path.parent/f"{new_path.stem}_formateado.txt")
    # guardado del texto formateado
    text_to_file(formated_text, path)
    print('Texto formateado!')
            

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    main(args.filepath, args.max_width, args.sobreescribir)
