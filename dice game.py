import random
import os
#........................................................................
import pyttsx3 #the main module.........  not a pre build module        .
                                        #                               .
engine=pyttsx3.init('sapi5')                #                           .
voices=engine.getProperty('voices')  #david voice.........#             .
engine.setProperty('voices',voices[0].id)#                              .
#                                                                       ..... the code for speech output
def speak(audio):                           #                           .
        engine.say(audio)                         #                     .
        engine.runAndWait() #speak code..........#                      .            
        return "None"                     #                             . 
# ....................................................................... 
print("there are 10 random number , lets see what do you get")
print("and in each of the number there is a massage for you ")
speak("this is, only a game, so dont take it seriously, than you will fail your exam")

name=input("enter your name")
speak("are you ready, "+name)
while True:
    randomnumber=random.randrange(1, 11)

    num=input("enter go to start otherwise type stop to exit the game") 
    if(num=="go"):
        print(randomnumber)
    elif(num=="stop"):
        exit()

    if(randomnumber==1):
        speak("hello "+name)
        speak("i have somthing for you")
        path= "D:\project\downloadrose.jpeg"                    
        os.startfile(path)
    elif(randomnumber==2):
        speak("well, i dont want to tell you, but you looks very ugly ")
        print("just kidding dont be serious")
        path= "D:\project\images.jpeg"                    
        os.startfile(path)
    elif(randomnumber==3):
        speak("i dont think, you are smart enough, to understand my source code")
        print("just kidding dont be serious")
        path= "D:\project\istockphoto-177841092-170667a.jpg"                    
        os.startfile(path)
    elif(randomnumber==4):
        speak("fuck you, bitch")
        print("just kidding dont be serious")
        path= "D:\project\download.jpeg"                    
        os.startfile(path)
    elif(randomnumber==5):
        speak("hy hello, i have something for you, take it")
        print("just kidding dont be serious")
        path= "D:\project\images (1).jpeg"                    
        os.startfile(path)
    elif(randomnumber==6):
        speak("hy your father is here he want to tell you somthing")
        print("just kidding dont be serious")
        path= "D:\project\download (1)ok.jpeg"                    
        os.startfile(path)
    elif(randomnumber==7):
        speak("wow, you are looking so handsome, ")
        print("just kidding dont be serious")
        path= "D:\project\download (1)handsome.jpeg"                    
        os.startfile(path)
    elif(randomnumber==8):
        speak("i have some advice for you , stop drinking alcohol and weed ")
        print("just kidding dont be serious")
        path= "D:\project\download (1).jpeg"                    
        os.startfile(path)
    elif(randomnumber==9):
        speak("wow, you are so smart ")
        print("just kidding dont be serious")
        path= "D:\project\images (2).jpeg"                    
        os.startfile(path)
    elif(randomnumber==10):
        speak("be happy with what you are")
        print("just kidding dont be serious")
        path= "D:\project\download (2).jpeg"                    
        os.startfile(path)
    
    
    
    
    
    
