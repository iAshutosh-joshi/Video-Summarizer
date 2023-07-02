import torch
from glob import glob
def transcript_gen():
    device = torch.device('cpu')  
    model, decoder, utils = torch.hub.load(repo_or_dir='snakers4/silero-models',
                                        model='silero_stt',
                                        language='en', 
                                        device=device)
    (read_batch, split_into_batches,
    read_audio, prepare_model_input) = utils  
    test_files = glob('./test_docs/ytaudio.wav')
    batches = split_into_batches(test_files, batch_size=10)
    input = prepare_model_input(read_batch(batches[0]),
                                device=device)

    output = model(input)
    transcript = ''
    for example in output:
        transcript = transcript + decoder(example.cpu()) + ' '
    return transcript