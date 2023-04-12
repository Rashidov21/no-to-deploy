from django import forms 
from .models import Article

class AddArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'tag', 'category', 'body']
        # exclude = ['slug', 'author','published','on_top','comments','views']
        widgets = {
            'title':forms.TextInput(attrs={"class":"form-control"}),
            'tag':forms.Select(attrs={"class":"form-select", "multiple":"", "aria-label":"multiple select example"}),
            'category':forms.Select(attrs={"class":"form-select"}),
            'body':forms.Textarea(attrs={"class":"form-control"}),            
        }
    
    # def save(self):
    #     instance = forms.ModelForm.save(self)
    #     instance.tag_set.add(*self.cleaned_data['tag'])
    #     return instance