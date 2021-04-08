import os
directorio = input("Ingresa ruta: ")
count, comandos = 1, []

with os.scandir(directorio) as ficheros:
    for fichero in ficheros:
        if fichero.is_file() and fichero.name.endswith('.tar.xz'):
            comando = f"gpg --armor --symmetric '{fichero.name}' && rm -vr '{fichero.name}' &&"
            comandos.append(comando)

print('date +"Inicio: %D %r" &&')

for com in comandos:
    print(f"echo '' && echo '   Archivo {count} de {len(comandos)}' && echo '' &&\n{com}")
    count+=1

print("date +'Finalizado: %D %r'")