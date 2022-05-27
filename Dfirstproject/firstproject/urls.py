from os import stat
from unicodedata import name
from django.contrib import admin
from django.urls import path
from Deutsch.views import List, detail
import Deutsch.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', List,name="list"),
    path('<int:pk>', detail,name="detail"),
    path('new/',Deutsch.views.new, name="new"),
    path('create/',Deutsch.views.create, name="create"),
    path('delete/<int:post_id>',Deutsch.views.delete,name="delete"),
    path('<int:post_id>/edit/',Deutsch.views.edit,name="edit"),
    path('<int:post_id>/update/',Deutsch.views.update,name="update"),
    path('<int:post_id>/comment', Deutsch.views.add_comment, name="add_comment"),
    path('<int:post_id>/comments/<int:comment_id>/delete/',Deutsch.views.delete_comment,name="delete_comment"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)