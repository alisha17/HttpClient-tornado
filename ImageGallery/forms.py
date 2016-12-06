from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class DeleteImageForm(forms.Form):
    image_id = forms.IntegerField()   
    
    