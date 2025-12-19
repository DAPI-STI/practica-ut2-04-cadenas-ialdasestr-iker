"""
Ejercicio 9: leer una fecha (día, mes, año) introducida como "dd/mm/aaaa"
y mostrar cada componente por separado.

La función:

Recibe un string con formato "d/m/aaaa" o "dd/mm/aaaa".

Devuelve (dia, mes, año) como enteros.

Si el formato o los rangos son incorrectos, lanza ValueError.
"""

def parse_date(date_str: str) -> tuple[int, int, int]:
    """Devuelve (día, mes, año) como enteros a partir de una cadena d/m/aaaa."""
    # TODO: usa split("/"), convierte a int y valida rangos sencillos
    date_str = date_str.strip()
    parte = date_str.split("/")
    
    if len(parte) != 3:

        raise ValueError("El formato tiene que ser d/m/aaaa")

    try:
        dia, mes, año = map(int, parte)

    except ValueError:

        raise ValueError("Los valores de la fecha tienen que ser completos")

    if not (1 <= dia <= 31):

        raise ValueError("El día esta comprendido entre 1 y 31")
    
    if not (1 <= mes <= 12):
    
        raise ValueError("El mes debe está comprendido entre 1 y 12")
    
    if año <= 0:
       
        raise ValueError("El año es positivo")

    return dia, mes, año
