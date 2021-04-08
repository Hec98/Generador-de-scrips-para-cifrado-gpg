import os
from datetime import datetime
directorio = input("Ingresa ruta: ")
i, count, index, comandos = 0, 1, [], []

with os.scandir(directorio) as ficheros:
    for fichero in ficheros:
        if not fichero.name.endswith('.tar.xz'):
            date = datetime.now().strftime('%d%m%Y%H%M%S') + str(i)
            name = date + " --> " + fichero.name
            index.append(name)  
            comando = f"tar -Jcvf '{date}.tar.xz' '{fichero.name}' && rm -vr '{fichero.name}' &&" 
            comandos.append(comando)
            i+=1
            
print("echo 'Index:")
for ind in index:
    print(f"{ind}")
print("' > Index.in.txt &&")

print('date +"Inicio: %D %r" &&')

for com in comandos:
    print(f"echo '' && echo '   Archivo {count} de {len(comandos)}' && echo '' &&\n{com}")
    count+=1

print(f"tar -Jcvf 'Index.in.txt.tar.xz' 'Index.in.txt' && rm -vr 'Index.in.txt' && date +'Finalizado: %D %r'")