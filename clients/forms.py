from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Comment here !',
            'rows': 4,
            'cols': 50
        }))

    class Meta:
        model = Comment
        fields = ['author']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('comment', 'author')
#
#         widgets = {
#             'comment': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.Textarea(attrs={'class': 'form-control'}),
#
#         }
