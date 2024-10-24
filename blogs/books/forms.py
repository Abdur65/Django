from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100) 
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if not email.endswith("@example.com"):
            raise forms.ValidationError("Email must be from example.com domain.")
        return email