from django.conf.urls import url
from .views import (NoteView, NoteCreateView, NoteDeleteView,
                    NoteUpdateView, NoteDetailView)

app_name = 'notes'

urlpatterns = [
    url(r'^$', NoteView.as_view(), name='notelist'),
    url(r'^create/', NoteCreateView.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)', NoteDeleteView.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)', NoteUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)', NoteDetailView.as_view(), name='detail'),
]

