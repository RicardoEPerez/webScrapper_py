import re
from colorama import Fore
import requests

website = 'http://futanarifreak.blogspot.com'

resultado = requests.get(website)
content = resultado.text
#print(content)

listaB = []

for x in range(1,22):
    patron = r"<b>"+str(x)+". [\w-]*"
    nombre = re.findall(patron, str(content))
    listaB.append(nombre)
    #print (nombre)

noDuplicate = list(set(listaB))

print(listaB)