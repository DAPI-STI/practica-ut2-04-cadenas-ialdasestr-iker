"""
Ejercicio 8: leer un precio con dos decimales y mostrar euros y céntimos por separado.

La función:

Recibe una cadena como "123.45" o "123,45".

Devuelve una tupla (euros, centimos) como enteros.

Valida que haya exactamente dos decimales; en caso contrario, ValueError.
"""

def euros_cents(price_str: str) -> tuple[int, int]:
    """Separa la parte entera (euros) y los céntimos a partir de una cadena."""
    # TODO: sustituye coma por punto, separa, valida y convierte a enteros
    price_str = price_str.strip().replace(",", ".")
    partes = price_str.split(".")
   
    if len(partes) != 2 or len(partes[1]) != 2:
        
        raise ValueError("El formato debe estar compuesto por dos decimales, ej: 431.76")
    
    try:
        euro = int(partes[0])
        centimos = int(partes[1])
    
    except ValueError:
    
        raise ValueError("Los valores tienen que ser numéricos")

    return euro, centimos