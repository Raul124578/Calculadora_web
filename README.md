Calculadora de Raíces de Polinomios

Aplicación web desarrollada en Django que permite calcular raíces de funciones usando métodos numéricos: **Bisección**, **Newton-Raphson** y **Newton-Raphson Modificado**. Incluye visualización de la gráfica del polinomio y una tabla de iteraciones.

Tecnologías Utilizadas
- Python 3.10+
- Django 4.x
- SymPy
- NumPy
- Matplotlib
- HTML/CSS (con Bootstrap opcional)


Instalación y Ejecución Local

Clona el repositorio:
git clone: https://github.com/Raul124578/calculadora

2.Crear y activar un entorno virtual
python -m venv env
source env/bin/activate    

3.Instala dependencias:
pip install -r requirements.txt

4.Corre  el servidor : python manage.py runserver
5.Accede a la app: http://127.0.0.1:8000/



Cómo usar la aplicación
1.	Ingresa la función polinómica (por ejemplo: x**3 - 2*x + 1).
2.	Selecciona el método numérico.
3.	Ingresa los parámetros necesarios (según el método).
4.	Visualiza la tabla de iteraciones, la raíz aproximada y la gráfica del polinomio.

Métodos implementados
•	Bisección
•	Newton-Raphson
•	Newton-Raphson Modificado

Estructura del proyecto
calculadora/
├── calculadora/          # Configuración del proyecto Django
├── calculadoraweb/       # Aplicación principal
│   ├── static/           # Archivos estáticos (gráficas)
│   ├── templates/        # Plantillas HTML
│   ├── forms.py          # Formulario del usuario
│   ├── views.py          # Lógica del cálculo
├── manage.py             # Script de administración
├── README.md             # Documentación principal

