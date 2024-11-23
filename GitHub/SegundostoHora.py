print ('Escriba una cantidad de segundos: ')
s=int(input())
h=s/3600
hor=s%3600
m=hor/60
seg=hor%60 
print (str(s),' segundos son ',int(h),' horas',int(m),' minutos y',int(seg),' segundos')
