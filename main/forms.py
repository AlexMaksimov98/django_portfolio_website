from django.forms import ModelForm
from .models import Message

class ContactForm(ModelForm):

    use_required_attribute = False

    class Meta:
        model = Message
        fields = '__all__'
        labels = {
            'name': 'Your name',
            'email': 'Your email',
            'text': 'Your message'
        }
        error_messages = {
            'name': {
                'required': 'Oops! You forgot to write your name!'
            },
            'email': {
                'required': 'Oops! You forgot to write your email!'
            },
            'text': {
                'required': 'Oops! You forgot to write your message!'
            }
        }
        