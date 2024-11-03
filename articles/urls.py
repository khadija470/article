from django.urls import path
##.parcequ ils sont dans le meme repertoire
from .views import home,useradmin,supprimer_article,modifier_article,newarticle
from django.conf.urls.static import static
from blog import settings
# ,newarticle
urlpatterns = [
    path("",home,name="home"),
    path("useradmin/",useradmin,name="useradmin"),
    path('supprimer_article/<int:article_id>/',supprimer_article, name='supprimer_article'),
    path('modifier_article/<int:article_id>/',modifier_article, name='modifier_article'),
    path("newarticle/",newarticle,name="newarticle")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
