from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Image, UploadForm
# from .forms import UploadForm


def index(request):
    return HttpResponseRedirect(reverse('imgup:upload'))


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = UploadForm()

    return render(request, 'imgup/upload.html', {'form': form, })


def gallery(request):
    return render(request, 'imgup/gallery.html', {'images': Image.objects.all, })
