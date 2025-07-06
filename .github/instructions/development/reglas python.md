# Reglas de Python

## Estilo de Código

### PEP 8 - Guía de Estilo
- Usar 4 espacios para indentación (no tabs)
- Longitud máxima de línea: 79 caracteres
- Dos líneas en blanco antes de definiciones de clase
- Una línea en blanco antes de definiciones de función

### Nomenclatura
- **Variables y funciones**: `snake_case`
- **Clases**: `PascalCase`
- **Constantes**: `UPPER_SNAKE_CASE`
- **Módulos**: `lowercase` o `snake_case`

## Buenas Prácticas

### Imports
```python
# Orden de imports:
# 1. Librerías estándar
# 2. Librerías de terceros
# 3. Módulos locales

import os
import sys

import requests
import numpy as np

from .utils import helper_function
```

### Funciones
- Una función debe hacer una sola cosa
- Usar docstrings para documentar
- Nombres descriptivos
- Máximo 20 líneas por función

### Variables
- Nombres descriptivos y claros
- Evitar variables globales
- Usar type hints cuando sea posible

## Estructura de Archivos

### Orden en archivos Python
1. Shebang y encoding
2. Docstring del módulo
3. Imports
4. Constantes
5. Clases
6. Funciones
7. Código principal (`if __name__ == "__main__":`)

## Manejo de Errores
- Usar excepciones específicas
- No usar `except:` genérico
- Limpiar recursos con `try/finally` o `with`

## Comentarios
- Comentarios claros y concisos
- Actualizar comentarios al cambiar código
- Evitar comentarios obvios