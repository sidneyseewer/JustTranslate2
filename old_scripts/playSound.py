
import simpleaudio as sa

# Load the .wav file
wave_obj = sa.WaveObject.from_wave_file("test.wav")

# Play the sound
play_obj = wave_obj.play()

# Wait for the sound to finish playing
play_obj.wait_done()
