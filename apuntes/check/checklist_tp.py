import json
import os
import sys

# Forzar UTF-8 en la consola de Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    os.system("chcp 65001 > nul")

# ──────────────────────────────────────────────
#  ARCHIVO DE GUARDADO
# ──────────────────────────────────────────────
ARCHIVO = os.path.join(os.path.dirname(__file__), "checklist_tp_data.json")

# ──────────────────────────────────────────────
#  CHECKLIST INICIAL
# ──────────────────────────────────────────────
CHECKLIST_INICIAL = {
    "📁 Estructura del Proyecto": [
        "Crear index.html y style.css raíz",
        "Carpeta css/ con archivos CSS",
        "Carpeta img/ con todas las imágenes",
        "Carpeta js/ (opcional)",
        "Google Font importada y aplicada",
        "Mínimo 2 iconos (Bootstrap Icons / Font Awesome)",
        "Navbar con enlaces # en el header",
        "1 componente de Bootstrap (máximo)",
        "Meta tag viewport en el <head>",
        "Secciones conectadas por anclas #seccion",
    ],
    "🏠 Sección 1 — Home": [
        "Imagen principal: ancho >= 80%, alto >= 1/3 pantalla",
        "Header con navbar",
        "Títulos semánticos (h1, h2...)",
        "Textos descriptivos",
        "Footer",
    ],
    "🃏 Sección 2 — Cards": [
        "Mínimo 2 cards",
        "Cada card: imagen + título + texto",
        "Botón en las cards",
    ],
    "🖼️ Sección 3 — Galería": [
        "Mínimo 7 imágenes en grilla",
        "Título de sección",
        "Layout con Grid o Flex",
    ],
    "📬 Sección 4 — Contacto": [
        "Input: Nombre",
        "Input: Email",
        "Input: Teléfono",
        "Textarea: Comentario",
        "Select (selector desplegable)",
        "Radio o Checkbox",
        "Labels para cada campo",
        "Botón Enviar",
        "Botón Reset",
    ],
    "⚙️ Consideraciones Generales": [
        "Cada sección ocupa mínimo 100vh",
        "IDs y clases usadas correctamente",
        "Flex y/o Grid implementados",
        "Código correctamente indentado",
        "Comentarios en HTML y CSS",
        "Responsive: 360px / 768px / 1024px con mediaqueries",
    ],
    "🚀 Entrega": [
        "Repositorio Git subido a GitHub",
        "Deploy en GitHub Pages / Netlify / Vercel",
        "Link funcional y accesible",
    ],
}

# ──────────────────────────────────────────────
#  COLORES (consola Windows compatible)
# ──────────────────────────────────────────────
VERDE   = "\033[92m"
ROJO    = "\033[91m"
AMARILLO= "\033[93m"
CYAN    = "\033[96m"
BLANCO  = "\033[97m"
GRIS    = "\033[90m"
RESET   = "\033[0m"
NEGRITA = "\033[1m"

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# ──────────────────────────────────────────────
#  CARGA / GUARDADO
# ──────────────────────────────────────────────
def cargar_datos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    # Primera vez: construir estructura desde CHECKLIST_INICIAL
    datos = {}
    for seccion, items in CHECKLIST_INICIAL.items():
        datos[seccion] = [{"texto": item, "hecho": False} for item in items]
    guardar_datos(datos)
    return datos

def guardar_datos(datos):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(datos, f, ensure_ascii=False, indent=2)

# ──────────────────────────────────────────────
#  ESTADÍSTICAS
# ──────────────────────────────────────────────
def calcular_progreso(datos):
    total = sum(len(items) for items in datos.values())
    hechos = sum(1 for items in datos.values() for i in items if i["hecho"])
    return hechos, total

def barra_progreso(hechos, total, ancho=30):
    if total == 0:
        return ""
    porcentaje = hechos / total
    llenos = int(porcentaje * ancho)
    barra = "█" * llenos + "░" * (ancho - llenos)
    color = VERDE if porcentaje == 1 else AMARILLO if porcentaje >= 0.5 else ROJO
    return f"{color}[{barra}]{RESET} {NEGRITA}{hechos}/{total}{RESET} ({porcentaje*100:.0f}%)"

# ──────────────────────────────────────────────
#  MOSTRAR CHECKLIST
# ──────────────────────────────────────────────
def mostrar_checklist(datos):
    limpiar()
    hechos, total = calcular_progreso(datos)
    print(f"\n{NEGRITA}{CYAN}{'='*55}{RESET}")
    print(f"{NEGRITA}{CYAN}   CHECKLIST TP MAQUETACIÓN UTN — Entrega 21/04/2026{RESET}")
    print(f"{NEGRITA}{CYAN}{'='*55}{RESET}")
    print(f"  Progreso total: {barra_progreso(hechos, total)}\n")

    num_global = 1
    for seccion, items in datos.items():
        hechos_sec = sum(1 for i in items if i["hecho"])
        color_sec = VERDE if hechos_sec == len(items) else AMARILLO
        print(f"{color_sec}{NEGRITA}  {seccion}  [{hechos_sec}/{len(items)}]{RESET}")
        for item in items:
            estado = f"{VERDE}[✔]{RESET}" if item["hecho"] else f"{ROJO}[ ]{RESET}"
            texto  = f"{GRIS}{item['texto']}{RESET}" if item["hecho"] else item["texto"]
            print(f"    {GRIS}{num_global:02d}.{RESET} {estado} {texto}")
            num_global += 1
        print()

# ──────────────────────────────────────────────
#  MENÚ PRINCIPAL
# ──────────────────────────────────────────────
def mostrar_menu():
    print(f"{NEGRITA}{BLANCO}  ¿Qué querés hacer?{RESET}")
    print(f"  {CYAN}[M]{RESET} Marcar / desmarcar un ítem")
    print(f"  {CYAN}[A]{RESET} Agregar ítem personalizado")
    print(f"  {CYAN}[E]{RESET} Eliminar ítem personalizado")
    print(f"  {CYAN}[R]{RESET} Resetear todo el checklist")
    print(f"  {CYAN}[S]{RESET} Salir")
    print(f"\n{GRIS}  (los cambios se guardan automáticamente){RESET}")
    return input(f"\n  {NEGRITA}Opción: {RESET}").strip().upper()

# ──────────────────────────────────────────────
#  ACCIONES
# ──────────────────────────────────────────────
def marcar_item(datos):
    try:
        n = int(input(f"\n  {AMARILLO}Número de ítem a marcar/desmarcar: {RESET}"))
        num = 1
        for items in datos.values():
            for item in items:
                if num == n:
                    item["hecho"] = not item["hecho"]
                    estado = f"{VERDE}✔ COMPLETADO{RESET}" if item["hecho"] else f"{ROJO}✘ PENDIENTE{RESET}"
                    print(f"\n  {estado}: {item['texto']}")
                    guardar_datos(datos)
                    input(f"\n  {GRIS}[Enter para continuar]{RESET}")
                    return
                num += 1
        print(f"\n  {ROJO}Número fuera de rango.{RESET}")
        input(f"  {GRIS}[Enter para continuar]{RESET}")
    except ValueError:
        print(f"\n  {ROJO}Ingresá un número válido.{RESET}")
        input(f"  {GRIS}[Enter para continuar]{RESET}")

def agregar_item(datos):
    print(f"\n  {AMARILLO}Secciones disponibles:{RESET}")
    secciones = list(datos.keys())
    for i, s in enumerate(secciones, 1):
        print(f"    {CYAN}{i}.{RESET} {s}")

    # Opción para crear sección nueva
    print(f"    {CYAN}{len(secciones)+1}.{RESET} ➕ Crear sección nueva")

    try:
        op = int(input(f"\n  {AMARILLO}Elegí sección (número): {RESET}"))
        if op == len(secciones) + 1:
            nueva_sec = input(f"  {AMARILLO}Nombre de la nueva sección: {RESET}").strip()
            if not nueva_sec:
                print(f"\n  {ROJO}Nombre vacío, cancelado.{RESET}")
                input(f"  {GRIS}[Enter para continuar]{RESET}")
                return
            datos[nueva_sec] = []
            secciones = list(datos.keys())
            seccion = nueva_sec
        elif 1 <= op <= len(secciones):
            seccion = secciones[op - 1]
        else:
            raise ValueError

        texto = input(f"  {AMARILLO}Texto del nuevo ítem: {RESET}").strip()
        if not texto:
            print(f"\n  {ROJO}Texto vacío, cancelado.{RESET}")
            input(f"  {GRIS}[Enter para continuar]{RESET}")
            return

        datos[seccion].append({"texto": texto, "hecho": False})
        guardar_datos(datos)
        print(f"\n  {VERDE}✔ Ítem agregado en «{seccion}»{RESET}")
        input(f"  {GRIS}[Enter para continuar]{RESET}")

    except ValueError:
        print(f"\n  {ROJO}Opción inválida.{RESET}")
        input(f"  {GRIS}[Enter para continuar]{RESET}")

def eliminar_item(datos):
    try:
        n = int(input(f"\n  {AMARILLO}Número de ítem a eliminar: {RESET}"))
        num = 1
        for seccion, items in datos.items():
            for i, item in enumerate(items):
                if num == n:
                    confirmacion = input(
                        f"\n  {ROJO}¿Eliminar «{item['texto']}»? (s/n): {RESET}"
                    ).strip().lower()
                    if confirmacion == "s":
                        items.pop(i)
                        guardar_datos(datos)
                        print(f"  {VERDE}Ítem eliminado.{RESET}")
                    else:
                        print(f"  Cancelado.")
                    input(f"  {GRIS}[Enter para continuar]{RESET}")
                    return
                num += 1
        print(f"\n  {ROJO}Número fuera de rango.{RESET}")
        input(f"  {GRIS}[Enter para continuar]{RESET}")
    except ValueError:
        print(f"\n  {ROJO}Ingresá un número válido.{RESET}")
        input(f"  {GRIS}[Enter para continuar]{RESET}")

def resetear(datos):
    conf = input(f"\n  {ROJO}¿Resetear TODOS los ítems a pendiente? (s/n): {RESET}").strip().lower()
    if conf == "s":
        for items in datos.values():
            for item in items:
                item["hecho"] = False
        guardar_datos(datos)
        print(f"  {VERDE}Checklist reseteado.{RESET}")
    else:
        print(f"  Cancelado.")
    input(f"  {GRIS}[Enter para continuar]{RESET}")

# ──────────────────────────────────────────────
#  MAIN
# ──────────────────────────────────────────────
def main():
    # Habilitar colores ANSI en Windows
    os.system("color")

    datos = cargar_datos()

    while True:
        mostrar_checklist(datos)
        opcion = mostrar_menu()

        if opcion == "M":
            marcar_item(datos)
        elif opcion == "A":
            agregar_item(datos)
        elif opcion == "E":
            eliminar_item(datos)
        elif opcion == "R":
            resetear(datos)
        elif opcion == "S":
            limpiar()
            hechos, total = calcular_progreso(datos)
            print(f"\n  {CYAN}Progreso final: {barra_progreso(hechos, total)}{RESET}")
            print(f"  {GRIS}Datos guardados en: {ARCHIVO}{RESET}\n")
            break
        else:
            print(f"\n  {ROJO}Opción no válida.{RESET}")
            input(f"  {GRIS}[Enter para continuar]{RESET}")

if __name__ == "__main__":
    main()
