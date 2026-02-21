## 👋 ¡Bienvenidos usuarios a mi proyecto! sistema de intentos limitados

<img src="imagen_presentacion.png" alt="Presentación" width="205" align="left" style="margin-right:20px; border-radius:5px;">  
<p style="text-align: justify;">

Este proyecto consiste en el desarrollo de un **sistema de autenticación con intentos limitados** utilizando Python. El programa solicita al usuario un nombre de usuario y una contraseña, permitiendo únicamente un número máximo de intentos antes de bloquear el acceso al sistema.

El sistema valida las credenciales ingresadas comparándolas con datos previamente definidos. Si el usuario introduce información incorrecta, el programa muestra un mensaje de error y reduce el número de intentos disponibles, simulando el comportamiento básico de un sistema de seguridad real.

Este proyecto está orientado a reforzar la lógica de control en programas interactivos, permitiendo comprender cómo manejar errores, limitar acciones del usuario y finalizar procesos de manera controlada.

#
### 🧑‍💻 Lenguaje de programacion
- Python

#
### 🎯 Objetivos del proyecto
- El objetivo principal es fortalecer el uso de **bucles while**, **estructuras condicionales** y **operadores lógicos**.
- además de comprender cómo implementar restricciones de acceso mediante intentos limitados en un programa de consola.

#
### 🧠 Temas que se a aplicado
- Variables
- Entrada de datos (`input`)
- Estructuras condicionales (`if`, `else`)
- Bucles (`while`)
- Operadores lógicos (`and`)
- Control de flujo
- Validación de credenciales

#
### ⚙️ Funcionamiento
1. El programa solicita al usuario un nombre de usuario y una contraseña.
2. Se compara la información ingresada con las credenciales correctas.
3. Si los datos son incorrectos, se descuenta un intento y se muestra un mensaje.
4. El proceso se repite hasta que:
   - Las credenciales sean correctas, o
   - Se agoten los intentos permitidos.
5. Si los intentos se agotan, el sistema bloquea el acceso y finaliza el programa.

#
### ▶️ Cómo usar el proyecto
Tienes dos opciones para obtener el código:
1. **Descargar directamente:**
   Haz clic en el botón verde code y selecciona download zip.

2. **Clonar con git:**
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
   ```