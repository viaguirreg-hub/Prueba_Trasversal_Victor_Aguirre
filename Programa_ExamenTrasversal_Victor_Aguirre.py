def leer_opcion():
    while True:
        try:
            val = int(input("Ingrese opción: "))
            if 1 <= val <= 6: return val
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def asientos_origen(origen, r, v):
    ori_find = origen.strip().upper()
    total = sum(v[k][1] for k in r if r[k][0].upper() == ori_find and k in v)
    print(f"El total de asientos disponibles es: {total}")

def busqueda_precio(p_min, p_max, r, v):
    res = [f"{r[k][0]}-{r[k][1]}--{k}" for k in v if p_min <= v[k][0] <= p_max and v[k][1] > 0 and k in r]
    if res: print(f"Los recorridos encontrados son: {sorted(res)}")
    else: print("No hay recorridos en ese rango de precios.")

def buscar_codigo(codigo, v):
    return any(k.upper() == codigo.strip().upper() for k in v)

def actualizar_precio(codigo, nuevo_precio, v):
    for k in v:
        if k.upper() == codigo.strip().upper():
            v[k][0] = nuevo_precio
            return True
    return False

def validar_codigo(c, r): return len(c.strip()) > 0 and not any(k.upper() == c.strip().upper() for k in r)
def validar_origen(o): return len(o.strip()) > 0
def validar_destino(d): return len(d.strip()) > 0
def validar_distancia(di): return di > 0
def validar_tipo_bus(tb): return tb in ['normal', 'semi-cama', 'cama']

def agregar_recorrido(codigo, o, d, di, tb, s, wf, pr, asn, r, v):
    if buscar_codigo(codigo, v): return False
    k = codigo.strip().upper()
    r[k], v[k] = [o, d, di, tb, s, wf], [pr, asn]
    return True

def eliminar_recorrido(codigo, r, v):
    for k in list(v.keys()):
        if k.upper() == codigo.strip().upper():
            r.pop(k); v.pop(k)
            return True
    return False

def main():
    r = {'R001': ['Santiago', 'Valparaiso', 120, 'normal', 'dia', True]}
    v = {'R001': [7990, 20]}
    
    while True:
        print("\nMENÚ PRINCIPAL\n1. Asientos por ciudad de origen\n2. Búsqueda de recorridos por rango de precio\n3. Actualizar precio de recorrido\n4. Agregar recorrido\n5. Eliminar recorrido\n6. Salir")
        op = leer_opcion()
        if op == 1:
            asientos_origen(input("Ingrese ciudad: "), r, v)
        elif op == 2:
            while True:
                try:
                    p1, p2 = int(input("Mínimo: ")), int(input("Máximo: "))
                    break
                except ValueError: print("Debe ingresar valores enteros")
            busqueda_precio(p1, p2, r, v)
        elif op == 3:
            while True:
                cod = input("Ingrese código: ")
                try:
                    pr = int(input("Nuevo precio: "))
                    if pr > 0: print("Precio actualizado" if actualizar_precio(cod, pr, v) else "El código no existe")
                    else: print("Invalido")
                except ValueError: print("Debe ingresar valores enteros")
                if input("¿Repetir? (s/n): ").strip().lower() != 's': break
        elif op == 4:
            c, o, d = input("Código: "), input("Origen: "), input("Destino: ")
            try: di = int(input("Distancia: "))
            except ValueError: di = -1
            tb, s, wf = input("Bus: ").lower().strip(), input("Servicio: ").lower().strip(), input("WiFi (s/n): ").lower().strip()
            try: pr, asn = int(input("Precio: ")), int(input("Asientos: "))
            except ValueError: pr, asn = -1, -1
            
            if (validar_codigo(c, r) and validar_origen(o) and validar_destino(d) and 
                validar_distancia(di) and validar_tipo_bus(tb) and s in ['dia','noche'] and wf in ['s','n'] and pr > 0 and asn >= 0):
                agregar_recorrido(c, o, d, di, tb, s, wf=='s', pr, asn, r, v)
                print("Recorrido agregado")
            else: print("Validación rechazada.")
        elif op == 5:
            print("Recorrido eliminado" if eliminar_recorrido(input("Código: "), r, v) else "El código no existe")
        elif op == 6:
            print("Programa finalizado.")
            break

main()