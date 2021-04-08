import os
directorio = input("Ingresa ruta: ")
count, comandos = 1, []

with os.scandir(directorio) as ficheros:
    for fichero in ficheros:
        if fichero.is_file() and fichero.name.endswith('.tar.xz'):
            comando = f"tar -Jxvf '{fichero.name}' && rm -vr '{fichero.name}' &&" 
            comandos.append(comando)
        
print('date +"Inicio: %D %r" &&')

for com in comandos:
    print(f"echo '' && echo '   Archivo {count} de {len(comandos)}' && echo '' &&\n{com}")
    count+=1

print("if [ -f 'Index.in.txt' ]; \nthen \nrm -v Index.in.txt \nfi && date +'Finalizado: %D %r'")
