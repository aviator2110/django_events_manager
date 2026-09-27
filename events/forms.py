from django import forms

class EventForm(forms.Form):
    CATEGORY_CHOICES = [
        ('Education', 'Образование'),
        ('Technology', 'Технологии'),
        ('Sport', 'Спорт'),
        ('Entertainment', 'Развлечения'),
        ('Other', 'Другое'),
    ]
    STATUS_CHOICES = [
        ('upcoming', 'Предстоящее'),
        ('open_for_registration', 'Открыто для регистрации'),
        ('ongoing', 'В процессе'),
        ('completed', 'Завершено'),
        ('cancelled', 'Отменено'),
        ('planned', 'Запланировано'),
    ]
    BAD_WORDS = ["вонючка", "тупица", "дурак"]

    title = forms.CharField(min_length=10, max_length=100, label="Название")
    description = forms.CharField(min_length=10, max_length=500, label="Описание")
    location = forms.CharField(min_length=10, max_length=200, label="Место")
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, label="Категория")
    status = forms.ChoiceField(choices=STATUS_CHOICES, label="Статус")

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 10:
            raise forms.ValidationError("Название должно быть не менее 10 символов")
        for word in self.BAD_WORDS:
            if word in title.lower():
                raise forms.ValidationError("В названии есть запрещенные слова")
        return title
    
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 10:
            raise forms.ValidationError("Описание должно быть не менее 10 символов")
        for word in self.BAD_WORDS:
            if word in description.lower():
                raise forms.ValidationError("В описании есть запрещенные слова")
        return description
    
    def clean_location(self):
        location = self.cleaned_data['location']
        if len(location) < 10:
            raise forms.ValidationError("Место должно быть не менее 10 символов")
        for word in self.BAD_WORDS:
            if word in location.lower():
                raise forms.ValidationError("В месте есть запрещенные слова")
        return location

    
    def clean_status(self):
        new_status = self.cleaned_data.get('status')
        old_status = self.initial.get('status')
        if old_status == 'completed' and new_status != 'completed':
            raise forms.ValidationError("Нельзя изменить статус завершенного события")
        return new_status