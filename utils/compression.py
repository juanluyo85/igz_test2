# -*- coding: utf-8 -*-


def encode(in_str):
    """
    Esta función debe devolver el string codificado de la siguiente manera:
    Por cada grupo de caracteres alfabéticos (de la A a la Z sin incluir la Ñ y sin distinguir mayúsculas
    de minúsculas) iguales consecutivos, se incluira dicho caracter en mayúsculas seguido del número de repeticiones.
    Por ejemplo para la entrada "aaAabaccCBb", la salida debe ser "A4B1A1C3B2"
    :param in_str: string de entrada. Estará formado por letras de la A a la Z sin incluir la Ñ
    :return: string codificado como se describe más arriba
    """
    in_str = in_str.upper()
    current_char = in_str[0]
    current_count = 0
    out_str = ''
    for ch in in_str:
        if(ch == current_char):
            current_count += 1
        else:
            out_str += current_char + str(current_count)
            current_count = 1
            current_char = ch  
    out_str += current_char + str(current_count)
    return out_str