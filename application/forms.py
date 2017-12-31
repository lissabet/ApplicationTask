from django import forms
from .models import Items, AttachmentImage, Category

class ItemForm(forms.ModelForm):
    image = forms.ImageField(label='Загрузите изображение', required=False)
    title = forms.CharField(max_length=255, label='Наименование')
    category = forms.ModelChoiceField(label='Выберите категорию', empty_label=None, queryset=Category.objects.all())
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 3}),
                                  required=False,
                                  label='Описание товара')

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['image'].widget.attrs.update({
            'class': 'form-control form-item',
        })
        self.fields['title'].widget.attrs.update({
            'class': 'form-control form-item',
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control form-item',
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control form-item',
        })


    def save(self, commit=True):
        super(ItemForm, self).save(self)
        attachment = AttachmentImage(title=self.cleaned_data['image'], image=self.cleaned_data['image'])
        attachment.save()
        self.instance.image.add(attachment)


    class Meta:
        model = Items
        fields = ('title', 'category', 'description')