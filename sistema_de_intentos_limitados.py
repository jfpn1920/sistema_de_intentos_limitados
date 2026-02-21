usuario_correcto = "admin"
contrasena_correcta = "1234"
intentos_maximos = 3
intentos = 0
while intentos < intentos_maximos:
    usuario = input("ingrese su usuario: ")
    contrasena = input("ingrese su contraseña: ")
    if usuario == usuario_correcto and contrasena == contrasena_correcta:
        print("acceso concedido, bienvenido al sistema.")
        break
    else:
        intentos += 1
        intentos_restantes = intentos_maximos - intentos
        print(f"datos incorrectos, intentos restantes: {intentos_restantes}")
if intentos == intentos_maximos:
    print("acceso bloqueado, se agotaron los intentos permitidos.")