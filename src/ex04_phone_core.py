"""
Ejercicio 4: a partir de un teléfono con el formato "+34-<numero>-<extension>"
obtener solamente la parte central (el número), sin prefijo ni extensión.

Ejemplo: "+34-913724710-56" -> "913724710"
"""

def phone_core(s: str) -> str:
    """
    Recibe el teléfono como cadena y devuelve solo la parte central.
    Requisitos mínimos (si no se cumplen, lanza ValueError):
    - Debe haber exactamente 3 partes separadas por "-".
    - La primera parte debe comenzar por "+" (prefijo).
    - La parte central debe ser numérica.
    """
    # TODO: usa .strip(), .split("-") y validaciones con .isdigit() y startswith("+")
    s = s.strip()
    parte = s.split("-")


    # Validaciones
    if len(parte) != 3:
        raise ValueError("El número de teléfono es incorrecto")


    if not parte[0].startswith("+"):
        raise ValueError("  El número debe empezar con el símbolo "+"")


    if not parte[1].isdigit():
        raise ValueError("La parte central no puede tener letras, ni símcolos")

    return parte[1]
