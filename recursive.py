import math
import sys


def calcular_cost_pont(h, alpha, beta, coordenadas, i=1, cost=0):
    longitud = len(coordenadas)
    if i >= longitud:
        d_dos = coordenadas[longitud - 1][0] - coordenadas[0][0]
        r_dos = d_dos / 2
        altura_ultim = h - coordenadas[longitud - 1][1]
        altura_primer = h - coordenadas[0][1]
        dos_pilares = 0
        if r_dos <= altura_ultim and r_dos <= altura_primer:
            altura_doble = altura_ultim + altura_primer
            dos_pilares = altura_doble * alpha + (d_dos * d_dos) * beta

        if cost <= dos_pilares:
            return cost
        else:
            return dos_pilares

    sum_d = 0
    d = coordenadas[i][0] - coordenadas[i - 1][0]
    sum_d += d * d
    r = d / 2
    altura1 = h - coordenadas[i][1]
    altura2 = h - coordenadas[i - 1][1]
    if i == 1:
        altura = altura1 + altura2
    else:
        altura = altura1

    cost += altura * alpha + d * d * beta
    if r > altura1 or r > altura2:
        d = coordenadas[longitud - 1][0] - coordenadas[0][0]
        r = d / 2
        if r <= altura1 and r <= altura2:
            x = coordenadas[0][0]
            y = coordenadas[0][1]
            distancia = math.sqrt(abs((x * x + y * y) - d * d + r * r))
            if r < distancia and y > r:
                return "impossible"
            altura = altura1 + altura2
            cost = altura * alpha + d * d * beta
            return cost
        else:
            return "impossible"
    else:
        i = i + 1
        return calcular_cost_pont(h, alpha, beta, coordenadas, i, cost)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        parametros = f.readline().split()
        h = int(parametros[1])
        alpha = int(parametros[2])
        beta = int(parametros[3])
        lista = []
        for coordenada in f.readlines():
            coordenadas = coordenada.split()
            coordenadas = list(map(int, coordenadas))
            lista.append(coordenadas)
        print(calcular_cost_pont(h, alpha, beta, lista))


if __name__ == '__main__':
    main()

