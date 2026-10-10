# Obtención de Tipo de Cambio (Banxico)

## 1. Objetivo del Script
El objetivo de este script (`main.py`) es consultar de manera automatizada el tipo de cambio oficial (dólar estadounidense a peso mexicano - serie FIX `SF43718`) del día actual mediante el servicio API REST del Banco de México (Banxico). 

El script realiza la petición HTTP autenticada con un token de acceso, valida la respuesta y mapea la información a estructuras de datos tipadas (`dataclasses`) para imprimir el valor del tipo de cambio en consola.

---

## 2. Requisitos del Sistema
* **Python**: Versión `3.14.8` (definida en el archivo `.python-version`).

---

## 3. Librerías Utilizadas e Instalación

El proyecto utiliza las siguientes librerías externas:

* **`requests`**: Utilizada para realizar solicitudes HTTP a la API REST de Banxico.
* **`dacite`**: Utilizada para convertir y validar diccionarios de respuesta JSON en objetos estructurados (`dataclasses`).
* **`python-dotenv`**: Utilizada para cargar variables de entorno desde un archivo `.env`.

> *Nota: Módulos como `datetime`, `dataclasses`, `typing` y `os` forman parte de la biblioteca estándar de Python y no requieren instalación adicional.*

### Ejemplos de Instalación

Puedes instalar las librerías necesarias con `pip`:

**Instalación conjunta:**
```bash
pip install requests dacite python-dotenv
```

**Instalación individual:**
```bash
pip install requests
pip install dacite
pip install python-dotenv
```

*(Opcional) Si utilizas un entorno virtual:*
```bash
python -m venv venv
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate

pip install requests dacite python-dotenv
```

---

## 4. Generación y Configuración del Token de Banxico

Para consumir la API de Banxico es indispensable contar con un token de autenticación (`Bmx-Token`).

1. **Generar Token**:
   * Solicita tu token de acceso en: [Generación de Token de Banxico](https://www.banxico.org.mx/SieAPIRest/service/v1/token).
2. **Configurar Variable de Entorno**:
   * Crea un archivo `.env` en la raíz del proyecto (basándote en `.env.example`):
     ```env
     TOKEN=tu_token_aqui
     ```

---

## 5. Documentación y Especificación de la API (Swagger)

Para consultar detalles técnicos adicionales, formatos de respuesta y catálogo de series disponibles:

* **Swagger UI / Documentación interactiva**: [Banxico SieAPIRest Swagger](https://www.banxico.org.mx/SieAPIRest/swagger/index.html)

---

## 6. Ejecución del Script

Una vez configurado el token y las dependencias, ejecuta:

```bash
python main.py
```
