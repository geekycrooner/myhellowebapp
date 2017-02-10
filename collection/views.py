from django.shortcuts import render, redirect
from collection.forms import VerseForm
from collection.models import Verse

def index(request):
  verses = Verse.objects.all()
  return render(request, 'index.html', {
    'verses': verses,
  })

def verse_detail(request, slug):
  verse = Verse.objects.get(slug=slug)
  return render(request, 'verses/verse_detail.html', {
    'verse': verse,
  })

def edit_verse(request, slug):
  # grab the object 
  verse = Verse.objects.get(slug=slug)
  # set the form we're using 
  form_class = VerseForm

  # if we're coming to this view from a submitted form
  if request.method == 'POST':
    # grab the data from the submitted form and apply to the form
    form = form_class(data=request.POST, instance=verse)
    if form.is_valid():
      # save the new data
      form.save()
      return redirect('verse_detail', slug=verse.slug)
  # otherwise just create the form
  else:
    form = form_class(instance=verse)
  # and render the template
  return render(request, 'verses/edit_verse.html', {
    'verse': verse,
    'form': form,
  })
