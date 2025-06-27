def read_file_to_dict(filename):
    diccionario = {}
    try:
        with open(datos, 'r') as file:
            l = file.readline()
            inicio = 0
            for i in range(len(l)):
                if linea[i] == ";":
                    venta = l[inicio:i]
                    a = venta.find(":")
                    if a != -1:
                        clave = venta[:a]
                        valor = float(venta[a+1:])
                        if clave not in diccionario:
                            diccionario[clave] = [valor]
                        else:
                            diccionario[clave].append(valor)
                    inicio = i+1
        return diccionario
    except FileNotFoundError:
        raise FileNotFoundError



def process_dict(data):
    for producto, elementos in data.items():
        a =0
        for b in elementos:
            a = float(a + b)
            promedio = a/len(elementos)
        elementos = a
        print(f"{producto}: ventas totales ${elementos:.2f}, promedio ${promedio:.2f}")
