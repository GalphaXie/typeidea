from ckeditor.widgets import CKEditorWidget
from dal import autocomplete
from django import forms

from blog.models import Category, Tag, Post


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=autocomplete.ModelSelect2(url='category-autocomplete'),
        label='分类',
    )
    tag = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(url='tag-autocomplete'),
        label='标签',
    )
    content = forms.CharField(widget=CKEditorWidget(), label="正文", required=True)

    class Meta:
        model = Post
        fields = ('desc', 'category', 'tag', 'title', 'content', 'status')
