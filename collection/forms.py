from django.forms import ModelForm

from collection.models import Verse

class VerseForm(ModelForm):
  class Meta:
    model = Verse
    fields = ('ref','text','version',)