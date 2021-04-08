# Generar clave pública y privada
gpg --full-generate-key

# Exportar la clave pública
gpg -a --export micorreo@dominio.com > clave.gpg.asc

nota: clave.gpg.asc cuyo contenido podemos ver y compartir libremente

# Importar clave de otro usuario
gpg --import clave.gpg.asc

nota: se puede cifrar con la clave de este usuario

# Cifrar archivo de manera asimétrica
gpg -a -r correo.del.destinatario@asd.com --encrypt nombreDelArchivo

# Eliminar archivo original con srm -> sudo apt install secure-delete
srm -vr nombearchivo-carpeta

# Descifrar archivos
gpg -a --decrypt archivoEncriptado > archivoDesencriptado

# Ligas de consulta
https://parzibyte.me/blog/2019/05/21/cifrar-descifrar-archivos-linux-gpg/

https://parzibyte.me/blog/2019/06/05/cifrado-asimetrico-gpg-linux-tutorial-ejemplos/

## Uso de Generador de Srips
python3 comprimirRemoverArchivos.py
--Ingresar directorio: /Documentos/ejemplo
python3 descomprimirRemoverArchivos.py
--Ingresar directorio: /Documentos/ejemplo
python3 cifrado.py
--Ingresar directorio: /Documentos/ejemplo
python3 decifrado.py
--Ingresar directorio: /Documentos/ejemplo
