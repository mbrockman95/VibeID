import freesound, sys,os

client = freesound.FreesoundClient()
client.set_token("8B01Qr77J2Z911rWyOz852g5mZOo4fJxBiw23LMC","token")

results = client.text_search(query="dubstep",fields="id,name,previews")

for sound in results:
    sound.retrieve_preview(".",sound.name+".mp3")
    print(sound.name)