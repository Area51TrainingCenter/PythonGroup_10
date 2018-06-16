from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import View
from django.views.generic import FormView, UpdateView

from usuarios.forms import RegistroForm
from usuarios.models import Perfil as PerfilModel, Favorito
from productos.models import Producto


class Registro(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm
    success_url = '/'

    def form_valid(self, form):
        usuario = form.save()
        perfil = PerfilModel()
        perfil.usuario = usuario
        perfil.direccion = form.cleaned_data['direccion']
        perfil.telefono = form.cleaned_data['telefono']
        perfil.dni = form.cleaned_data['dni']
        perfil.save()

        login(self.request, usuario, 'django.contrib.auth.backends.ModelBackend')

        return super().form_valid(form)


class Perfil(UpdateView):
    template_name = 'perfil.html'
    model = PerfilModel
    fields = ('direccion', 'telefono', 'dni',)
    success_url = '/perfil'

    def get_object(self, queryset=None):
        return self.request.user.perfil


class AgregarFavoritos(View):
    def get(self, request, **kwargs):
        favorito = Favorito()
        favorito.usuario = request.user
        favorito.producto = Producto.objects.get(pk=kwargs['pk'])
        favorito.save()
        return redirect('detalle', pk=kwargs['pk'])


class QuitarFavoritos(View):
    def get(self, request, **kwargs):
        request.user.favorito_set.filter(producto_id=kwargs['pk']).delete()
        return redirect('detalle', pk=kwargs['pk'])
