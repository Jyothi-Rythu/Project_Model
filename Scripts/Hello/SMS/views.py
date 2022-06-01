from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import SMS

def index(request):
  mymembers = SMS.objects.all().values()
  template = loader.get_template('f1.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
  
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
  
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = SMS(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('index'))

def delete(request, id):
  member = SMS.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('index'))
