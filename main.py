import threading
from motor import Motor
from ocr_webcam import OCR_Webcam

motor = Motor()

def command_to_angle(command):
    # Example of possible command
    if(command == "rotate 10"):
        rotate(10)

if __name__ == '__main__':
    texto = "no text recognized"
    
    webcam = OCR_Webcam()
    
    camera_thread = threading.Thread(target=webcam.main_loop(command_to_angle))
    camera_thread.start()
