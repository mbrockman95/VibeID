import ffmpeg
import glob

#for filename in glob.glob('*.mp3'):
#   print(filename)

stream = ffmpeg.input('Dubstep Growl.mp3')
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, 'output.wav')
ffmpeg.run(stream)