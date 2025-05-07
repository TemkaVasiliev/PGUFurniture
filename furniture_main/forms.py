from django import forms
from .models import Article as Post

class FeedbackForm(forms.Form):
    name = forms.CharField(label="Ваше имя", max_length=100, required=True)
    
    email = forms.EmailField(label="Ваш email", required=True)
    
    usability = forms.ChoiceField(
        label="Оцените удобство сайта",
        choices=[
            ('отлично', 'Отлично'),
            ('хорошо', 'Хорошо'),
            ('удовлетворительно', 'Удовлетворительно'),
            ('плохо', 'Плохо')
        ],
        widget=forms.RadioSelect,
        required=True
    )
    
    liked_sections = forms.MultipleChoiceField(
        label="Какие разделы сайта вам понравились?",
        choices=[
            ('новости', 'Новости'),
            ('статьи', 'Статьи'),
            ('блог', 'Блог'),
            ('форум', 'Форум')
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    
    visit_frequency = forms.ChoiceField(
        label="Как часто вы посещаете сайт?",
        choices=[
            ('ежедневно', 'Ежедневно'),
            ('несколько раз в неделю', 'Несколько раз в неделю'),
            ('раз в неделю', 'Раз в неделю'),
            ('реже', 'Реже')
        ],
        widget=forms.Select,
        required=True
    )
    
    comments = forms.CharField(
        label="Ваши комментарии и пожелания",
        widget=forms.Textarea,
        required=False
    )
    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Имя не должно содержать цифры.")
        return name


from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Оставить комментарий...'}),
        }
        labels = {
            'text': '',
        }
