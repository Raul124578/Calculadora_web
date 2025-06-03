from django import forms

METODO_CHOICES = [
    ('biseccion', 'Bisección'),
    ('newton', 'Newton-Raphson'),
    ('newton_mod', 'Newton-Raphson Modificado'),
]

class MetodoForm(forms.Form):
    funcion = forms.CharField(label='Función (f(x))', max_length=100)
    metodo = forms.ChoiceField(label='Método', choices=METODO_CHOICES)
    a = forms.FloatField(label='Extremo inferior (a)', required=False)
    b = forms.FloatField(label='Extremo superior (b)', required=False)
    x0 = forms.FloatField(label='Valor inicial (x₀)', required=False)
    tolerancia = forms.FloatField(label='Tolerancia (error permitido)')
    max_iter = forms.IntegerField(label='Máximo número de iteraciones')

