from pytube import YouTube
import ffmpeg
import os
from huggingsound import SpeechRecognitionModel
import torch
import librosa
import soundfile as sf
import transformers
from transformers import BartTokenizer, BartForConditionalGeneration, pipeline

def summarize_text_model():
    import subprocess
    import torch
    import librosa
    import soundfile as sf
    from transformers import pipeline, BartTokenizer, BartForConditionalGeneration

    subprocess.run(['ffmpeg', '-i', './test_docs/video.mp4', '-acodec', 'pcm_s16le', '-ar', '16000', '-y', './test_docs/ytaudio.wav'], check=True)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    device
    model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device=device)
    input_file = './test_docs/ytaudio.wav'
    print(librosa.get_samplerate(input_file))
    stream = librosa.stream(input_file, block_length=30, frame_length=16000, hop_length=16000)
    for i, speech in enumerate(stream):
        sf.write(f'{i}.wav', speech, 16000)
    audio_path =[]
    for a in range(i+1):
        audio_path.append(f'./{a}.wav')
    print(audio_path)
    transcriptions = model.transcribe(audio_path)
    full_transcript = ' '
    for item in transcriptions:
        full_transcript += ''.join(item['transcription'])
    print(len(full_transcript))
    tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')
    model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
    input_tensor = tokenizer.encode(full_transcript, return_tensors="pt", max_length=512)
    outputs_tensor = model.generate(input_tensor, max_length=160, min_length=120, length_penalty=2.0, num_beams=4, early_stopping=True)
    summarizer = pipeline('summarization')
    n = 1000
    splitSummary = []
    i = 0
    print(full_transcript)
    for i in range(0, int(len(full_transcript)+1), 1000):
        print(i)  
        if i+1000 > len(full_transcript):
            split = full_transcript[i:]
            print(len(split))
            summary = summarizer(split, max_length=180, min_length=30)
            splitSummary.append(summary)
        else:
            split = full_transcript[i: i+1000]
            summary = summarizer(split, max_length=180, min_length=30)
            splitSummary.append(summary)
    summaryText = ""
    for i in range(len(splitSummary)):
        summaryText = summaryText + splitSummary[i][0]['summary_text']
    return summaryText

