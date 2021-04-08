import os
directorio = input("Ingresa ruta: ")
count, comandos = 1, []

with os.scandir(directorio) as ficheros:
    for fichero in ficheros:
        if not fichero.name.endswith('.tar.xz'):
            comando = f"tar -Jcvf '{fichero.name}.tar.xz' '{fichero.name}' && rm -vr '{fichero.name}' &&"
            comandos.append(comando)

print("echo '' && date +'Inicio: %D %r' &&")

for com in comandos:
    print(f"echo '' && echo '   Archivo {count} de {len(comandos)}' && echo '' &&\n{com}")
    count+=1

print("date +'Finalizado: %D %r'")
