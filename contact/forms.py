from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A class for the contact form
    """
    class Meta:
        """
        A class for Meta information
        """
        model = Contact
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholders and classes, remove auto-generated
    #     labels and set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'default_name': 'Name',
    #         'default_email': 'Email',
    #         'default_subject': 'Subject',
    #         'default_message': 'Message',
    #     }
