from django import forms
#from captcha.fields import ReCaptchaField
#from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}), label='Your Name')
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}), label='Your Email')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone'}), label='Your Phone')
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': "I'm interested in ..."}), label='Your Message')
    # captcha = ReCaptchaField(
    #     widget=ReCaptchaV2Checkbox(
    #         attrs={
    #             'data-callback': 'recaptchaSuccess',
    #         }
    #     )
    # )