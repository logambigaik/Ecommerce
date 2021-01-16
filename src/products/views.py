#from django.views import ListView
from django.views.generic import ListView, DetailView

from django.shortcuts import render,get_object_or_404

from .models import Product

# Create your views here.

class ProductListView(ListView):
    queryset  = Product.objects.all()
    template_name = "product/list.html"

    """
    def get_context_data(self,*args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args,**kwargs)
        print(context)
        return context
    """
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
      # 'qs': queryset
       'object_list' : queryset
    }
    return render(request,'product/list.html',context)

class ProductDetailView(DetailView):
    queryset  = Product.objects.all()
    template_name = "product/detail.html"

    def get_context_data(self,*args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args,**kwargs)
        print(context)
        #context['abc'] ='abc'
        return context
    

def product_detail_view(request,pk=None,*args,**kwargs):
    '''
    print(kwargs)    #primary key is dictionary format
    print(args)
    '''
    queryset = Product.objects.get(pk=pk)  # instead pk=pk  can use id=pk too
    queryset =  get_object_or_404(Product,pk=pk)
    print(queryset)

    context = {
      # 'qs': queryset
       'object' : queryset
    }
    return render(request,'product/detail.html',context)
