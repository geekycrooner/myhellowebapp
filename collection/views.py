from django.template.defaultfilters import slugify
from django.shortcuts import render, redirect
from collection.forms import VerseForm
from collection.models import Verse
from django.contrib.auth.decorators import login_required
from django.http import Http404

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

@login_required
def edit_verse(request, slug):
  # grab the object 
  verse = Verse.objects.get(slug=slug)

  # make sure the logged in user is the owner of the thing
  if thing.user != request.user:
    raise Http404
    
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

def create_verse(request):
  form_class = VerseForm

  # if we're coming from a submitted form, do this
  if request.method == 'POST':
    # grab the data from the submitted form and apply to the form
    form = form_class(request.POST)
    if form.is_valid():
      # create an instance but don't save yet
      verse = form.save(commit=False)

      # set the additional details
      verse.user = request.user
      verse.slug = slugify(verse.ref)

      # save the object
      verse.save()

      # redirect to our newly created verse
      return redirect('verse_detail', slug=verse.slug)
  # otherwise just create the form
  else:
    form = form_class()

  return render(request, 'verses/create_verse.html', {
    'form': form,
  })