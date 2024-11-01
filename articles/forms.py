from django import forms
from .models import Article
  
class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = ['titre','resume','contenu','image','prix_kilo','origine','disponible','quantite_disponible','mode_conservation','temps_livraison']
          widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de l\'article'}),
            'resume': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Résumé'}),
            'contenu': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Contenu de l\'article'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'prix_kilo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Prix par kilo'}),
            'origine': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Origine'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'quantite_disponible': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Quantité disponible'}),
            'mode_conservation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mode de conservation'}),
            'temps_livraison': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Temps de livraison en jours'}),
        }