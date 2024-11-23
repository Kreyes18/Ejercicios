def arepe(base, altura):
    peri=2*base + 2*altura
    area=base*altura
    perimetro=peri
    return perimetro, area
base=float(input('Digite el valor de la base del rectangulo'))
altura=float(input('Digite la alutra del rectangulo'))
perimetro, area=arepe(base, altura)
print('Perimetro: ',perimetro,' Area: ',area)
