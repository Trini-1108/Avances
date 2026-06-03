# Ingresar contraseña en un cajero automático:

# Entrada:
clave= "python123"
intento=""
intentos=0

#Proceso:
while intento != clave and intentos <3:
    intento=input("Ingresa tu contraseña:")
    intentos=intentos+1

    if intento != clave and intentos <3:
        print(f"Contraseña incorrecta, te quedan {3-intentos} intentos")
    elif intento==clave:
        print("ACESSO PERMITIDO")
    else:
        print("Cuenta bloqueada por tomar demasiados intentos fallidos")
