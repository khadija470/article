from django import forms
from .models import Article
  
class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = ['titre','resume','contenu','image','prix_kilo','origine','disponible','quantite_disponible','mode_conservation','temps_livraison']