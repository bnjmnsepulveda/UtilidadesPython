import os
import time
import requests
from bs4 import BeautifulSoup

#se obtiene abecedario desde sistema.
abecedario = map(chr, range(97, 123))
file = open("palabras_chilenas.txt","w")
#recorriendo abecedario
for x in abecedario:
    print('solicitando palabras con '+ x)
    try:
        req = requests.get('https://diccionariochileno.cl/terms/' + x)
        soup = BeautifulSoup(req.text, 'html.parser')
        palabras = soup.find(class_= 'terms')
        #buscando palabras desde dom de pagina
        for link in palabras.find_all('a',class_=False):#class_=False significa que el tag no tenga el atrinuto class
            file.write(link.text + os.linesep)
            print(link.text)
    except Exception as ex:
        print('error leyendo palabras con ' + x  + ' error' + str(ex))
        time.sleep(2)

file.close()



