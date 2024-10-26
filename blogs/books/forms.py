from django import forms
from books.models import Book


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100) 
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if not email.endswith("@example.com"):
            raise forms.ValidationError("Email must be from example.com domain.")
        return email
    
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'publication_date', 'price', 'author', 'publisher']
        
        def clean_price(self):
            price = self.cleaned_data.get('price')
            
            if price < 0:
                raise forms.ValidationError("The price must be positive")
            
            return price
        
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)