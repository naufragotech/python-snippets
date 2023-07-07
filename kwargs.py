# Sígueme para más videos! ↓ ↓ ↓
# Youtube:   @naufragotech
# Instagram: @naufragotech
# Tik Tok:   @naufragotech

# *** Cómo funcionan los **kwargs ***
def funcion_kwargs(**kwargs):
    almuerzo = "Hoy almorcé: \n"

    if "entrada" in kwargs:
        almuerzo += "De entrada: " \
                    f"{kwargs['entrada']}\n"

    if "segundo" in kwargs:
        almuerzo += "De segundo: " \
                    f"{kwargs['segundo']}\n"

    if "postre" in kwargs:
        almuerzo += "Y de postre: " \
                    f"{kwargs['postre']}"

    print(almuerzo)


funcion_kwargs(
    entrada="Papa a la huancaína",
    segundo="Tallarines verdes",
    postre="Mazamorra"
)
