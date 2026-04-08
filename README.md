# Proyecto: API y Frontend de Gestión de Usuarios

## Descripción

Este proyecto consiste en una aplicación web que permite gestionar usuarios mediante una API REST desarrollada en Flask y una interfaz frontend en JavaScript puro.

La aplicación permite:

- Crear usuarios
- Listar usuarios
- Buscar usuarios por nombre en tiempo real
- Consultar usuarios por email

Los datos se almacenan en un archivo JSON para mantener persistencia.

---

## Tecnologías utilizadas

- Python (Flask)
- Flask-CORS
- JavaScript (Vanilla)
- HTML5
- CSS3

---

## Estructura del proyecto

```
pruebas/
 ├── prueba.py
 ├── users.json
 ├── index.html
 ├── app.js
 ├── styles.css
 └── README.md
```

---

## Instalación

Instalar dependencias necesarias:

```
pip install flask flask-cors
```

---

## Ejecución del proyecto

### 1. Ejecutar backend

```
python prueba.py
```

---

### 2. Ejecutar frontend

En la misma carpeta:

```
python -m http.server 5500
```

Abrir en el navegador:

```
http://127.0.0.1:5500/index.html
```

---

## Uso con Postman

### Crear usuario

- Método: POST  
- Endpoint: /add-user  
- Body (JSON):

```
{
  "name": "Ana",
  "email": "ana@mail.com"
}
```

Validaciones:
- Email válido  
- Campos no vacíos  
- No permite duplicados  

---

### Obtener todos los usuarios

- Método: GET  
- Endpoint: /users  

---

### Obtener usuario por email

- Método: GET  
- Endpoint: /user/{email}  

Ejemplo:

```
/user/ana@mail.com
```

---

## Funcionalidad del frontend

- Consume el endpoint /users  
- Muestra usuarios en formato de tarjetas  
- Permite buscar usuarios por nombre  
- Filtrado en tiempo real  
- Manejo de estado de carga  
- Manejo de errores  

---

## Persistencia

Los datos se almacenan en el archivo:

```
users.json
```

Este archivo se actualiza automáticamente al agregar nuevos usuarios.

---

## Uso de Inteligencia Artificial

Se utilizó inteligencia artificial como apoyo en:

- Generación de la estructura del backend y frontend  
- Implementación de validaciones  
- Manejo de errores  
- Integración entre frontend y backend  

---
