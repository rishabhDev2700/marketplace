from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from accounts.models import User


class AccountCreationForm(UserCreationForm):
    '''Account creation form to add new users'''
    class Meta:
        '''Extra meta information'''
        model = User
        fields = ('email','full_name', 'password','is_seller','is_buyer')
        
class AccountChangeForm(UserChangeForm):
    '''Form for updating a user's details'''
    class Meta:
        '''Extra meta information'''
        model = User
        fields = ('full_name', 'password')