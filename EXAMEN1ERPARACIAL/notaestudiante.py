def otorgar_beca(nota):
    if nota > 95:
        return True
    else:
        return False
nota_estudiante = 95
if otorgar_beca(nota_estudiante):
    print("¡Felicidades! El estudiante recibe una beca.")
else:
    print("El estudiante no califica para recibir una beca.")
