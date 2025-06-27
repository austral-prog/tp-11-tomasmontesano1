def read_file_to_dict(filename):
    diccionario = dict()
    try:
        with open(datos, 'r') as file:
            linea = file.readline()
            inicio = 0
            for i in range(len(linea)):
                if linea[i] == ";":
                    venta = linea[inicio:i]
                    pos = venta.find(":")
                    if pos != -1:
                        key = venta[:pos]
                        value = float(venta[pos+1:])
                        if key not in diccionario:
                            diccionario[key] = [value]
                        else:
                            diccionario[key].append(value)
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
