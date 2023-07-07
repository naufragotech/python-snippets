# Sígueme para más videos! ↓ ↓ ↓
# Youtube:   @naufragotech
# Instagram: @naufragotech
# Tik Tok:   @naufragotech

# *** Cómo funcionan los *args ***
def funcion_args(*args):
    cuadrados = [i ** 2 for i in args]
    print(max(cuadrados))


funcion_args(1, 2, 3, 4, 5, 6, 7)
