import cv2
#import collections
import threading


MAX_FRAMES = 100

class Reader:
    def __init__(self, url):
        self.url = url
        self.thread_running = False

        self.current_frame = None # keep only the last frame instead of queuing them.

        self.start_thread = threading.Thread(target=self.start)
        self.start_thread.start()
    
    def start(self):
        self.thread_running = True
        self.cap = cv2.VideoCapture(self.url)
        while self.thread_running:
            if self.cap is not None and self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    self.current_frame = frame
                    
            else:
                self.thread_running = False
                self.cap = None
                return
    
    def stop(self):
        self.thread_running = False
        if self.cap is not None:
            self.cap.release()
    
    def retrieve_frame(self):
        return self.current_frame

