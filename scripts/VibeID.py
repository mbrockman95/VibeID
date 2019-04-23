import database_conversion as dbc
import subprocess
import sys, os



dbc.download()

os.system("audio-convert.sh")

os.chdir('outputs')
	
print("Current Working Directory " , os.getcwd())
os.system('wav_to_spectrogram.py')

