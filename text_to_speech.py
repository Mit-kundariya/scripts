'''
@author: mit kundariya
'''
import pyttsx3
greet =pyttsx3.init()

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    
    def hi():
        greet.say("Hello dear")
        greet.runAndWait()
        
    def HowRU():
        greet.say("I am fine dear, Thank you and What about you?")
        greet.runAndWait()
     
    def Bye():       
        greet.say("Bye , Have a nice day")
        greet.runAndWait() 
    
    purchaselist = []   
    def PurchaseAdd(AddtoList):
        purchaselist.append(AddtoList)
        print(AddtoList+" Added")
        greet.say(AddtoList +" Added to your Purchase List")
        greet.runAndWait()
        
    def PurchaseRemove(removeFromList):
        purchaselist.remove(removeFromList)
        print(removeFromList+" Removed")
        greet.say(removeFromList+" Removed from your Purchase List")
        greet.runAndWait()        
        
    def PurchaseRead():
        
        for i in range(len(purchaselist)):
            print(purchaselist[i])
            greet.say(purchaselist[i])
            greet.runAndWait()
       
    def Schedule():
        greet.say("You have one movie booking , one weekly meeting and a client review meeting")
        greet.runAndWait()
        
    def Movie():
        greet.say("You have booking of padmaavt at 10:15am at Mall of Mysore")
        greet.runAndWait()       
    
    while True:
        print("Say something")
        audio = r.listen(source)
        
        try:
            sentence = r.recognize_google(audio).lower()
            print(sentence)
            
            if("hi" in sentence or "hello" in sentence or "hey" in sentence):
                hi()
            if("how are you" in sentence):
                HowRU()
            if("bye" in sentence):
                Bye()
            if("purchase list" in sentence):
                list1=[]
                list1 = sentence.split()
                if("add" in sentence):
                    startAdd=list1.index("add")
                    endAdd = list1.index("into")
                    for i in range(startAdd+1,endAdd):
                        if(list1[i]!="and"):
                            PurchaseAdd(list1[i])
                        else:
                            pass
                elif("remove" in sentence):
                    startRemove=list1.index("remove")
                    endRemove = list1.index("from")
                    for i in range(startRemove+1,endRemove):
                        if(list1[i]!="and"):
                            PurchaseRemove(list1[i])
                        else:
                            pass
                elif("what" in sentence):
                    PurchaseRead()
                else:
                    greet.say("Dear this feature is not defined")
         
            if("schedule" in sentence):
                Schedule()
            if("movie" in sentence):
                Movie()
                   
        except:
            print("Sorry Dear!!! Couldn't hear you")   
            
