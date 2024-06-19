from . import views
from .views import *
from django.urls import path

urlpatterns = [
    path('text-to-speech', textToSpeech, name="text-to-speech"),
    path('speech-to-text', speechToText, name="speech-to-text"),
    path('delete-converted-text/<int:id>/', delete_converted_text, name='delete_converted_text'),
    path('open-file-explorer/', openFileExplorer, name='open_file_explorer'),
]