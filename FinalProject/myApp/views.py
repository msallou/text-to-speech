import os
import shutil # moving the .mp3 file to another location
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from gtts import gTTS # google translate's voice, text to speech
from .models import *
import datetime # in order to get the date when adding to the database
import assemblyai
from django.core.files.base import ContentFile

# mp3Path = "D:\\199652\\AP_CSP\\Code\\PythonCode\\FinalProject\\mp3_files"
mp3Path = "mp3_files"


def openFileExplorer(request):
    os.startfile(mp3Path)
    return redirect('text-to-speech')

def delete_converted_text(request, id):
    if request.method == 'POST':
        converted_text = PreviousTextToSpeech.objects.filter(id=id)
        converted_text.delete()
    return redirect('text-to-speech')

def textToSpeech(request):
    previous_texts = PreviousTextToSpeech.objects.all()

    if request.method == 'POST':
        text_to_convert = request.POST.get('text_to_convert')
        name = request.POST.get('fileName')
        print(f"File name: {name}")


        print(f'\nButton clicked! Text to convert: {text_to_convert}')
        
        if text_to_convert and text_to_convert != '':
            store_audio = gTTS(text=text_to_convert, lang='en')
            text_exists = PreviousTextToSpeech.objects.filter(text=text_to_convert).exists()
            # name = 'test'
            store_audio.save(f"{name}.mp3")
            shutil.move(f"{name}.mp3", f"{mp3Path}\{name}.mp3")
            os.system(f"start {mp3Path}\{name}.mp3")
            
            if text_exists:
                print(f"The text, {text_to_convert}, is already in the database")
            else:
                print(f"The text is not already in the database")
                now = datetime.datetime.now()
                PreviousTextToSpeech.objects.create(date=now, text=text_to_convert)
        else:
            print('there is no text to convert')

    context = {
        'previous_texts': previous_texts,
    }

    return render(request, "textToSpeech.html", context)

def speechToText(request):
    # if the user submitted the form AND a file upload
    if request.method == "POST" and request.FILES.get("filename"):
        # get the file
        uploaded_file = request.FILES["filename"]

        # read the uploaded file into memory, without saving to disk
        file_content = ContentFile(uploaded_file.read())

        # transcribe the audio file directly from memory
        assemblyai.settings.api_key = "2f0577cb3ca748f2bc996528e9dd3cce"
        transcriber = assemblyai.Transcriber()

        # assuming the transcriber can handle file-like objects
        transcript = transcriber.transcribe(file_content)

        # if the transcriber returns an error
        if transcript.status == assemblyai.TranscriptStatus.error:
            context = {"error": transcript.error}
        # if there is no error
        else:
            context = {"transcript": transcript.text}

        return render(request, "speechToText.html", context)

    return render(request, "speechToText.html")
