from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Comment


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        if self.fields['in_stock']:
            self.fields['in_stock'].initial = True
        self.fields['sku'].label = 'SKU*'
        self.fields['info'].label = 'Info (please separate each spec with a comma)'
        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-dark rounded-0'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('username', 'body')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'username': '',
            'body': 'Comment on this product...',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = placeholders[field]
                self.fields[field].label = False
                self.fields[field].widget.attrs['placeholder'] = placeholder
