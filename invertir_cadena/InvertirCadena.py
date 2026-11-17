def InvertirCadena(cadena: str) -> str:
    """
    Invierte el orden de los caracteres de una cadena.

    Parameters:
        cadena (str): Texto a invertir.

    Returns:
        str: Cadena invertida.

    Examples:
        >>> InvertirCadena("UNISON")
        'NOSINU'
    """
    return cadena[::-1]
cadena = str(input("Que palabra desea invertir? = "))
print (InvertirCadena(cadena))
