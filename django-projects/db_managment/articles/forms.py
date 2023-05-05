from django import forms 
from django.template.defaultfilters import slugify
from .models import Article, Tag


class AddArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title','category', 'body']

        # exclude = ['slug', 'author','published','on_top','comments','views']
        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'tag':forms.SelectMultiple(attrs={"class":"form-select", "multiple":"", "aria-label":"multiple select example"}),
            'category':forms.Select(attrs={"class":"form-select"}),
            'body':forms.Textarea(attrs={"class":"form-control"}),            
        }

    # def save(self, commit=True):
    #     self.instance.slug = slugify(self.instance.title)
                  
    
