from django.shortcuts import render
from collection.models import Verse

def index(request):
  verses = Verse.objects.all()

  return render(request, 'index.html', {
    'verses': verses,
  })
