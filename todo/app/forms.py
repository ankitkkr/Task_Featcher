from django.forms import ModelForm
from app.models import TODO

# Create the form class.
class TodoForm(ModelForm):
     class Meta:
         model = TODO
         fields = ['title', 'status', 'priority']