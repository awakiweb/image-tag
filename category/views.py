from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from .models import Category
from .forms import CategoryForm


class CategoryListView(generic.ListView):
    template_name = 'category/category_list.html'
    context_object_name = 'category_list'
    paginate_by = 5

    def get_queryset(self):
        return Category.objects.all()


class CategorySearchView(generic.ListView):
    template_name = 'category/category_list.html'
    context_object_name = 'category_list'

    def get_queryset(self, **kwargs):
        param = self.request.GET.get('txtsearch')
        return Category.objects.filter(name__icontains=param)


class CategoryCreate(CreateView):
    form_class = CategoryForm
    template_name = 'category/category_form.html'


class CategoryUpdate(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/category_form.html'


class CategoryDelete(UpdateView):
    model = Category
    fields = ['active']
    template_name = 'category/category_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['active'] = False
        return super(CategoryDelete, self).post(request, **kwargs)


class CategoryRestore(UpdateView):
    model = Category
    fields = ['active']
    template_name = 'category/category_confirm_restore.html'

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['active'] = True
        return super(CategoryRestore, self).post(request, **kwargs)
