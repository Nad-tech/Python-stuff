import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf

fs = 44100  # Sample rate

def record(duration, fileName):
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write(fileName + '.wav', fs, myrecording)  # Save as WAV file 

def play(f):
    filename = f + '.wav'
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing


def playOrRec():
    i = input("Press p to play.\nPress r to record.\nPress q to quit\n->")

    if i == 'p':
        fileName = input('\nEnter file name\n')
        print('Playing')
        play(fileName)
        print('Finished playing')
        return 0

    if i == 'r':
        duration = input('\nEnter duration\n')
        fileName = input('\nEnter file name\n')
        print('Recording')
        record(int(duration), str(fileName))
        print('Finished recording')
        return 0

    if i == 'q':
        return 1

i = playOrRec()

while i != 1:
    i = playOrRec()
