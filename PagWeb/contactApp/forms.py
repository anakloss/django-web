from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label='Nombre completo', max_length=50, required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Enter your name...'}))
    email = forms.CharField(label='Email', max_length=50, required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'name@example.com'}))
    phone = forms.IntegerField(label='Telefono', required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'type': 'tel', 'placeholder': '(123) 456-7890'}))
    message = forms.CharField(label='Mensaje', required=True,
        widget=forms.Textarea(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'Enter your message here...',
        'style': 'height: 10rem'}))
