from django import forms


class NewVoteForm(forms.Form):
    title_of_question = forms.CharField(
        label="Название",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите название вопроса',
                'class': 'form-control',
                'id': 'title_of_question'
            }
        )
    )
    first_variant = forms.CharField(
        label="Первый вариант ответа",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите первый вариант ответа',
                'class': 'form-control',
                'id': 'first_variant'
            }
        )
    )
    second_variant = forms.CharField(
        label="Второй вариант ответа",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите второй вариант ответа',
                'class': 'form-control',
                'id': 'second_variant'
            }
        )
    )
