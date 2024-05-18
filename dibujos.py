def get_dibujo(vidas: int) -> str:
    """
    Dibuja al muñeco.

    Args:
        vidas (int): La cantidad de vidas para saber que etapa del dibujo mostrar.
    """
    dibujo: str = ""

    if vidas == 6:
        dibujo = """
 |-----|
 |
 |
 |
 |
 |
 |
---
        """
    elif vidas == 5:
        dibujo = """
 |-----|
 |    ( )
 |
 |
 |
 |
 |
---
        """
    elif vidas == 4:
        dibujo = """
 |-----|
 |    ( )
 |     |
 |     |
 |     |
 |
 |
---
        """
    elif vidas == 3:
        dibujo = """
 |-----|
 |    ( )
 |     |
 |    /|
 |     |
 |
 |
---
        """
    elif vidas == 2:
        dibujo = """
 |-----|
 |    ( )
 |     |
 |    /|\\
 |     |
 |
 |
---
        """
    elif vidas == 1:
        dibujo = """
 |-----|
 |    ( )
 |     |
 |    /|\\
 |     |
 |    / 
 |
---
        """
    elif vidas == 0:
        dibujo = """
 |-----|
 |    ( )
 |     |
 |    /|\\
 |     |
 |    / \\
 |
---
        """
    return dibujo
