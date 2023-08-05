# Sígueme para más videos! ↓ ↓ ↓
# Youtube:   @naufragotech
# Instagram: @naufragotech
# Tik Tok:   @naufragotech

# *** Cómo usar for en Python - Pt 2 ***

letras1 = ["a", "b", "c", "d", "e"]
letras2 = ["c", "d", "b", "a", "e"]

if len(letras1) == len(letras2):
    for letra in letras1:
        if letra not in letras2:
            print("No son iguales")
            break

    else:
        print("Sí son iguales!")
