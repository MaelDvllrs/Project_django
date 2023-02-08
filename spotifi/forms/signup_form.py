from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Username',
            'type': 'text',
        })
        self.fields["email"].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Email',
            'type': 'email',
        })
        self.fields["first_name"].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Firstname',
            'type': 'text',
        })
        self.fields["last_name"].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Lastname',
            'type': 'text',
        })
        self.fields["password1"].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Password',
            'type': 'password',
        })
        self.fields["password2"].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Confirmation password',
            'type': 'password',
        })

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
