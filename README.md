# EcoTech Solutions - TP Final

Proyecto organizado en los tres ejercicios solicitados. Los ejercicios 1 y 2
usan solamente la biblioteca estándar de Python. El ejercicio 3 integra el
cálculo de emisiones con una aplicación Django.

## Requisitos

- Python 3.10 o superior
- Django 4.2 o superior para ejecutar la aplicación web

Instalación de Django:

```powershell
python -m pip install -r ejercicio_3_auditoria_web\requirements.txt
```

## Ejercicio 1: sensores

```powershell
python -m ejercicio_1_sensores.main
python -m unittest discover -s ejercicio_1_sensores -p "test_*.py"
```

## Ejercicio 2: catálogo

```powershell
python -m ejercicio_2_productos.main
python -m unittest discover -s ejercicio_2_productos -p "test_*.py"
```

El ejemplo escribe el catálogo en
`ejercicio_2_productos\catalogo_ecotech.json`.

## Ejercicio 3: auditoría y panel Django

```powershell
python -m unittest discover -s ejercicio_3_auditoria_web -p "test_*.py"
python -m ejercicio_3_auditoria_web.manage runserver
```

Abrir `http://127.0.0.1:8000/` para ver el panel.
