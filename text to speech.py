import tkinter as tk 
import tkinter.messagebox as massagebox
import speech_recognition as sr 
import threading
import pyaudio
import wave
import os

class speechtotext(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("speech to text conversation")

        self.record_button=tk.Button(self,text="Start recording",command=self.start_recording)
        self.record_button.pack(pady=20)

        self.stop_button=tk.Button(self,text="stop Recording",command=self.stop_recording,state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        self.convert_button=tk.Button(self,text="convert to text",command=self.convert_audio_to_text,state=tk.DISABLED)
        self.convert_button.pack(pady=5)


class SpeechToText(tk.Tk):
    def _init_(self):
        self.audio_file_path="reciding_audio.wav"
        self.recording=False

    def start_recording(self):
        self.recording=True
        self.record_button.config(state=tk.DISABLED)  
        self.stop_button.config(state=tk.NORMAL)  
        self.play_button.config(state=tk.DISABLED)
        self.convert_button.config(state=DISABLED)

        self.audio=pyaudio,pyaudio()
        self.strea=self.audio.open(format=pyaudio.paInt16,channels=1,rate=44100,input=True,frames_per_buffer=1024)
        self.frames=[]

        self.recording_thread=threading.thread(target=self.record)
        self.record_thread.start()


    def record(self):
        while self.recording:
            data=self.stream.read(1024)
            self.frames.append(data)

    def stop_recording(self):
        self.recording=False
        self.stream.stop_stream()
        self.stream.close()
        self.adio.terminate()

        wf=wave.open(self.audio_file_path,'wb')
        wf.setstampwidth(self.audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(b"".join(self.frames))       
        wf.close() 

        self.record_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.play_button.config(state=tk.NORMAL)
        self.convert_button.config(state=tk.NORMAL)   

    def play_recording(self):
        os.system(f"start {self.audio_file_path}")

    def convert_audio_to_text(self):
        r=sr.Recognizer()
        with sr.AudioFile(self.audio_file_path) as source:
            audio_data=r.record(source)
            try:
                text=r.recognize_google(audio_data) 
                massagebox.showinfo("speech to text",text)

            except sr.UnknownValueError:
                massagebox.showwarning("speech to text",f"Error occurred: {e}")
            except sr.RequestError as e:
                massagebox.showerror("speech to text",f"Error occurred: {e}")

    if __name__=="__main__":
        app=speechtotext()
        app.mainloop()                       
