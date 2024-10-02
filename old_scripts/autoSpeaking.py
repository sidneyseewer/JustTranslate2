import subprocess
import os
import simpleaudio as sa

def _generate_wav(text, lan):
    voices = os.listdir(os.path.join("voices",lan))
    onnx_files = [file for file in voices if file.endswith(".onnx")]
    voice = onnx_files[0]
    wav_filename = "test.wav"
    # Prepare the command to generate the wav file
    command = f'echo {text} | .\\piper\\piper.exe -m .\\voices\\{lan}\\{voice} -f {wav_filename}'

    # Run the command in the shell with encoding set to utf-8
    process = subprocess.run(command, shell=True, encoding='utf-8', errors='ignore')
    
    # Check if the command was successful
    if process.returncode == 0:
        print("WAV file generated successfully.")
        return wav_filename
    else:
        print("Error generating WAV file.")
        return None

def _play_sound(wav_filename):
    # Load the .wav file
    wave_obj = sa.WaveObject.from_wave_file(wave_file=wav_filename)
    # Play the sound
    play_obj = wave_obj.play()
    # Wait for the sound to finish playing
    play_obj.wait_done()
    os.remove(wav_filename)

def speak_text(text, lan):    
    # Generate the wav file
    wav_file = _generate_wav(text=text, lan=lan)
    
    # Play the generated wav file
    if wav_file:
        _play_sound(wav_file)

def test_languages():
    test_array = [
        ("de", "Ich bin 28 Jahre alt und mag schöne Autos und Stiefel."),  # German
        ("fr", "J'ai 28 ans et j'aime les belles voitures et les bottes."),  # French
        ("es", "Tengo 28 años y me gustan los coches bonitos y las botas."),  # Spanish
        ("ru", "Мне 28 лет, и мне нравятся красивые машины и ботинки.")  # Russian
    ]
    for test in test_array:
        speak_text(text=test[1],lan=test[0])


if __name__ == "__main__":
    test_languages()

