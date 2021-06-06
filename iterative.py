import math
import sys


def calcular_cost_pont(h, alpha, beta, coordenadas):
    altura = h - coordenadas[0][1]
    sum_d = 0
    cost_dos = 0
    cost_tots = 0
    possible_tots = True
    i = 1
    while i < len(coordenadas) and possible_tots:
        d = coordenadas[i][0] - coordenadas[i - 1][0]  # distancia entre pilars
        r = d / 2
        altura1 = h - coordenadas[i - 1][1]  # altura del pilar anterior a i
        altura2 = h - coordenadas[i][1]
        if r <= altura1 and r <= altura2:
            altura += h - coordenadas[i][1]
            sum_d += d * d
            i += 1
        else:
            print("impossible")
            return -1
    if possible_tots:
        cost_tots = sum_d * beta + altura * alpha

    possible_dos = True
    d = coordenadas[len(coordenadas) - 1][0] - coordenadas[0][0]  # distancia entre pilars
    r = d / 2
    altura1 = h - coordenadas[0][1]  # altura del pilar anterior a i
    altura2 = h - coordenadas[len(coordenadas) - 1][1]
    if r <= altura1 and r <= altura2:
        j = 1
        while j < len(coordenadas) and possible_dos:
            x = coordenadas[j][0]
            y = coordenadas[j][1]
            distancia = math.sqrt(abs((x * x + y * y) - d * d + r * r))
            if r < distancia and y > h - r:
                possible_dos = False
                print(x)
            j += 1
    if possible_dos:
        cost_dos = d * d * beta + (altura1 + altura2) * alpha
    if possible_tots or possible_dos:
        print(min(cost_dos, cost_tots))
        return min(cost_dos, cost_tots)
    else:
        print("impossible")
        return -1


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
        calcular_cost_pont(h, alpha, beta, lista)


if __name__ == '__main__':
    main()

