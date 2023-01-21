import pyaudio
import cv2 as cv
    
from display import Display

W = 1920 // 2
H = 1080 // 2

display = Display(W, H)

# Set up the audio stream
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16,
                channels=1,
                rate=44100,
                input=True,
                frames_per_buffer=1024)

cv.namedWindow("Audio Visualisation", cv.WINDOW_NORMAL)
cv.resizeWindow("Audio Visualisation", 800, 600)

# Start capturing audio
while True:
    data = stream.read(1024)
    # print(data)

# Close the audio stream
stream.stop_stream()
stream.close()
p.terminate()

if __name__ == "__main__":
    main()
