def calcularNota(calificación):
    if(calificación >= 0.9 and calificación <= 1.0):
        nota = "Sobresaliente"
    elif (calificación >= 0.8 and calificación < 0.9):
        nota = "Notable"
    elif (calificación >= 0.7 and calificación < 0.8):
        nota = "Bien"
    elif (calificación >= 0.6 and calificación < 0.7):
        nota = "Suficiente"
    elif (calificación >=0 and calificación < 0.6):
        nota = "Insuficiente"
    else:
        nota = "calificación no es válido"
    return nota

try: 
    calificación = float(input("Ingrese la calificación (0.01 - 1.00):"))
    nota = calcularNota(calificación)
    print("El grado de su calificación es:", nota)
except:
    print("Error, debe ingresar un valor númerico")


