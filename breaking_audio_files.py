# -*- coding: utf-8 -*-
"""Breaking Audio Files.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12uBMXI0w711T91bcYpYTHXkcoiFxbjmp
"""

# Commented out IPython magic to ensure Python compatibility.
# %%capture
# !pip install pydub

from pydub import AudioSegment
import os

# Set the length of each segment in milliseconds
segment_length = 30000

# Set the path to the folder containing the audio files
audio_folder = ''

# Set the path to the folder where the segmented audio files will be saved
output_folder = ''

# Loop through each audio file in the folder
for filename in os.listdir(audio_folder):
    if filename.endswith('.mp3') or filename.endswith('.wav'):
        # Load the audio file using PyDub
        audio = AudioSegment.from_file(audio_folder + filename)

        # Calculate the number of segments that can be created from the audio file
        num_segments = len(audio) // segment_length

        # Create a new folder with the same name as the audio file
        new_folder = os.path.join(output_folder, os.path.splitext(filename)[0])
        os.makedirs(new_folder, exist_ok=True)

        # Loop through each segment and save it as a new audio file
        for i in range(num_segments):
            start = i * segment_length
            end = (i + 1) * segment_length
            segment = audio[start:end]
            segment.export(os.path.join(new_folder, f'{i}.wav'), format='wav')

