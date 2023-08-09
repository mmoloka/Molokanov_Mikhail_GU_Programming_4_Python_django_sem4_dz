from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import ProductForms
from .models import Product
import logging

logger = logging.getLogger(__name__)


def product_form(request):
    if request.method == 'POST':
        form = ProductForms(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            add_date = form.cleaned_data['add_date']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Get Product: {name=}; {description[:30]=}; {price=}')
            product = Product(
                name=name, description=description, price=price,
                quantity=quantity, add_date=add_date, image=image)
            product.save()
            msg = 'Product is saved.'
    else:
        form = ProductForms()
        msg = 'Fill out the form.'
    return render(request, 'fourth_app/product_form.html', {'form': form, 'msg': msg})
