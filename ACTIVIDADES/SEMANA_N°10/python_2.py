import random

def jugar():
    print("=" * 40)
    print("   🎯 JUEGO: ADIVINA EL NÚMERO")
    print("=" * 40)

    # Elegir dificultad
    print("\nElige una dificultad:")
    print("  1. Fácil   (1 - 50,  10 intentos)")
    print("  2. Medio   (1 - 100,  7 intentos)")
    print("  3. Difícil (1 - 200,  5 intentos)")

    dificultad = input("\nOpción (1/2/3): ").strip()

    if dificultad == "1":
        limite, intentos_max = 50, 10
    elif dificultad == "3":
        limite, intentos_max = 200, 5
    else:
        limite, intentos_max = 100, 7  # Medio por defecto

    numero_secreto = random.randint(1, limite)
    intentos = 0

    print(f"\n¡He pensado un número del 1 al {limite}!")
    print(f"Tienes {intentos_max} intentos. ¡Buena suerte!\n")

    while intentos < intentos_max:
        restantes = intentos_max - intentos

        try:
            intento = int(input(f"[{restantes} intento(s) restantes] Tu número: "))
        except ValueError:
            print("⚠️  Por favor ingresa un número válido.\n")
            continue

        if intento < 1 or intento > limite:
            print(f"⚠️  El número debe estar entre 1 y {limite}.\n")
            continue

        intentos += 1

        if intento == numero_secreto:
            print(f"\n🎉 ¡Correcto! ¡Adivinaste en {intentos} intento(s)!")
            if intentos == 1:
                print("🏆 ¡Increíble, lo lograste al primer intento!")
            elif intentos <= intentos_max // 2:
                print("⭐ ¡Excelente resultado!")
            return

        elif intento < numero_secreto:
            diferencia = numero_secreto - intento
            if diferencia <= 5:
                print("🔥 ¡Muy cerca! El número es un poco MÁS alto.\n")
            else:
                print("📈 El número es MÁS alto.\n")
        else:
            diferencia = intento - numero_secreto
            if diferencia <= 5:
                print("🔥 ¡Muy cerca! El número es un poco MÁS bajo.\n")
            else:
                print("📉 El número es MÁS bajo.\n")

    print(f"\n😞 ¡Se acabaron los intentos! El número era: {numero_secreto}")


def main():
    while True:
        jugar()
        print()
        otra = input("¿Quieres jugar de nuevo? (s/n): ").strip().lower()
        if otra != "s":
            print("\n👋 ¡Hasta la próxima!")
            break
        print()

if __name__ == "__main__":
    main()