from django.contrib import admin

# import your model
from collection.models import Verse

# set up automated slug creation
class VerseAdmin(admin.ModelAdmin):
  model = Verse
  list_display = ('ref', 'text', 'version',)
  prepopulated_fields = {'slug': ('ref',)}

# and register it
admin.site.register(Verse, VerseAdmin)
