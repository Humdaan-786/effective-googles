# Python program to translate
# speech to text and text to speech 
# pip install pygooglenews --upgrade
# pip install pyttsx3
# pip install SpeechRecognition


import speech_recognition as sr
import pyttsx3 
from pygooglenews import GoogleNews

# Initialize the recognizer 
r = sr.Recognizer() 
# Function to convert text to
# speech
def SpeakText(command):
      
    # Initialize the engine
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(command) 
    engine.runAndWait()


def get_titles(search):
    stories = []
    gn = GoogleNews(country='IN')
    search = gn.search(search)
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'title': item.title,
            'link':item.link
        }
        stories.append(story)
    return stories       

    # return

# Loop infinitely for user to
# speak
  
while(1):    
      
    # Exception handling to handle
    # exceptions at the runtime
    try:
          
        # use the microphone as source for input.
        with sr.Microphone() as source2:
              
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level 
            r.adjust_for_ambient_noise(source2, duration=0.2)
              
            #listens for the user's input 
            audio2 = r.listen(source2)
              
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
  
            print("You said: "+MyText)
            # SpeakText("Showing Results for "+ MyText)
            break

              
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
          
    except sr.UnknownValueError:
        
        SpeakText("What do you want to search")


print(get_titles(MyText))    
n=1
# for news in range(len(get_titles(MyText))):
#     SpeakText("News number  "+str(n) +"for"+ MyText)
#     SpeakText(get_titles(MyText)[news])
#     # "News number  "+str(n) +"for"+ MyText +"is"+

for i in get_titles(MyText) :
    SpeakText("News number  "+str(n) +"for"+ MyText)
    SpeakText(i['title'])
    n+=1