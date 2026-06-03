while True:
    # ============================================
    #   SISTEMA DE FINANCIAMIENTO - CONCESIONARIO
    # ============================================

    puntaje_total = 0

    # ── DATO 1: Ingreso Mensual ──────────────────
    ingreso = float(input("Ingrese su ingreso mensual (S/): "))

    if ingreso < 2000:
        puntaje_total += 5
        print("  → Puntaje por ingreso: 5 puntos")
    elif ingreso <= 5000:
        puntaje_total += 10
        print("  → Puntaje por ingreso: 10 puntos")
    else:
        puntaje_total += 20
        print("  → Puntaje por ingreso: 20 puntos")

    # ── DATO 2: Situación Laboral ────────────────
    print("\nSituación laboral:")
    print("  1. Desempleado")
    print("  2. Independiente")
    print("  3. Dependiente (en planilla)")
    situacion = int(input("Seleccione una opción (1/2/3): "))

    if situacion == 1:
        puntaje_total += 0
        print("  → Puntaje por situación laboral: 0 puntos")
    elif situacion == 2:
        puntaje_total += 8
        print("  → Puntaje por situación laboral: 8 puntos")
    elif situacion == 3:
        puntaje_total += 14
        print("  → Puntaje por situación laboral: 14 puntos")
    else:
        print("  ⚠ Opción inválida, se asigna 0 puntos")

    # ── DATO 3: Inicial Disponible ───────────────
    tiene_inicial = input("\n¿Tiene inicial disponible? (si/no): ").strip().lower()

    if tiene_inicial == "si":
        puntaje_total += 6
        print("  → Puntaje por inicial: 6 puntos")
    else:
        puntaje_total += 0
        print("  → Puntaje por inicial: 0 puntos")

    # ── RESULTADO FINAL ──────────────────────────
    print("\n============================================")
    print(f"  PUNTAJE TOTAL OBTENIDO: {puntaje_total} puntos")
    print("============================================")

    if puntaje_total > 25:
        print("  RESULTADO: ✅ FINANCIAMIENTO APROBADO")
    else:
        print("  RESULTADO: ❌ FINANCIAMIENTO DENEGADO")

    print("============================================")

    # ── PREGUNTA DE REPETICIÓN ───────────────────
    repetir = input("\n¿Desea evaluar otro cliente? (si/no): ").strip().lower()
    if repetir != "si":
        print("\n👋 Gracias por usar el sistema. ¡Hasta luego!")
        break