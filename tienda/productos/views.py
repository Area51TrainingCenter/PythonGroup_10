from django.views.generic import TemplateView, DetailView, ListView
from django.db.models import Q

from productos.models import Producto


# def home(request):
#     return HttpResponse('Hello')


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['productos'] = Producto.objects.all()[:5]
        return contexto


class Detalle(DetailView):
    template_name = 'detalle.html'
    model = Producto
    context_object_name = 'producto'

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['favorito'] = self.request.user.favorito_set.filter(producto=self.get_object()).exists()
        return contexto


class Buscador(ListView):
    template_name = 'buscador.html'
    model = Producto
    context_object_name = 'productos'

    def get_queryset(self):
        termino = self.request.GET.get('termino')
        productos = super().get_queryset()

        if not termino:
            return productos.none()

        productos = productos.filter(Q(nombre__icontains=termino) | Q(descripcion__icontains=termino))
        return productos
