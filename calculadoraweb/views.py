from django.shortcuts import render

# FIX para evitar RuntimeError con matplotlib
import matplotlib
matplotlib.use('Agg')

# Create your views here.

from .forms import MetodoForm
import numpy as np
import matplotlib.pyplot as plt
from sympy import sympify, lambdify, Symbol, diff
import uuid
import os

def index(request):
    form = MetodoForm()
    return render(request, 'calculadoraweb/index.html', {'form': form})

def calcular(request):
    if request.method == 'POST':
        form = MetodoForm(request.POST)
        if form.is_valid():
            funcion_str = form.cleaned_data['funcion']
            metodo = form.cleaned_data['metodo']
            tol = form.cleaned_data['tolerancia']
            max_iter = form.cleaned_data['max_iter']
            a = form.cleaned_data.get('a')
            b = form.cleaned_data.get('b')
            x0 = form.cleaned_data.get('x0')

            x = Symbol('x')
            f = sympify(funcion_str)
            f_lamb = lambdify(x, f, 'numpy')
            df = diff(f)
            df_lamb = lambdify(x, df, 'numpy')
            ddf = diff(df)
            ddf_lamb = lambdify(x, ddf, 'numpy')

            tabla = []
            raiz = None
            error = None
            mensaje = None

            try:
                if metodo == 'biseccion':
                    if f_lamb(a) * f_lamb(b) > 0:
                        raise ValueError("No hay cambio de signo en [a,b]")
                    for i in range(1, max_iter+1):
                        c = (a + b) / 2
                        fc = f_lamb(c)
                        error = abs(b - a) / 2
                        tabla.append((i, a, b, c, fc, error))
                        if error < tol or fc == 0:
                            raiz = c
                            break
                        if f_lamb(a) * fc < 0:
                            b = c
                        else:
                            a = c
                elif metodo == 'newton':
                    for i in range(1, max_iter+1):
                        fx = f_lamb(x0)
                        dfx = df_lamb(x0)
                        if dfx == 0:
                            raise ValueError("Derivada cero en iteración {}".format(i))
                        x1 = x0 - fx / dfx
                        error = abs(x1 - x0)
                        tabla.append((i, x0, fx, dfx, x1, error))
                        if error < tol:
                            raiz = x1
                            break
                        x0 = x1
                elif metodo == 'newton_mod':
                    dfx0 = df_lamb(x0)
                    ddfx0 = ddf_lamb(x0)
                    for i in range(1, max_iter+1):
                        fx = f_lamb(x0)
                        x1 = x0 - (fx * dfx0) / (dfx0**2 - fx * ddfx0)
                        error = abs(x1 - x0)
                        tabla.append((i, x0, fx, x1, error))
                        if error < tol:
                            raiz = x1
                            break
                        x0 = x1
                else:
                    mensaje = "Método no reconocido."
            except Exception as e:
                mensaje = str(e)
            # Definir encabezados para la tabla
            if metodo == 'biseccion':
                encabezados = ['Iteración', 'a', 'b', 'c', 'f(c)', 'Error']
            elif metodo == 'newton':
                encabezados = ['Iteración', 'x₀', 'f(x₀)', "f'(x₀)", 'x₁', 'Error']
            elif metodo == 'newton_mod':
                encabezados = ['Iteración', 'x₀', 'f(x₀)', 'x₁', 'Error']
            else:
                encabezados = []

            # Crear gráfica
            nombre = f"{uuid.uuid4()}.png"
            ruta = f"calculadoraweb/static/{nombre}"
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f_lamb(x_vals)
            plt.figure()
            plt.plot(x_vals, y_vals, label="f(x)")
            if raiz is not None:
                plt.axvline(raiz, color='r', linestyle='--', label="Raíz")
            plt.axhline(0, color='black')
            plt.title("Gráfica del Polinomio")
            plt.legend()
            plt.grid()
            plt.savefig(ruta)
            plt.close()

            return render(request, 'calculadoraweb/resultado.html', {
                'form': form,
                'tabla': tabla,
                'raiz': raiz,
                'grafica': nombre,
                'mensaje': mensaje,
                'encabezados': encabezados
            })
    else:
        form = MetodoForm()
    return render(request, 'calculadoraweb/index.html', {'form': form})
