import speech_recognition as sr
import pyttsx3 as py
import smtplib as sm
import mysql.connector
engine = py.init()

listener =sr.Recognizer()
engine = py.init()


class Email:
    check = 0
    to1 = 0

    def talk(this,text):
        engine = py.init()
        engine.say(text, 145)
        engine.runAndWait()



    def mic(self,question, check):

        listener = sr.Recognizer()
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            e.talk(question)
            print("listening.....")
            voice = listener.listen(source)
            try:
                answer = listener.recognize_google(voice)
                print(answer)
            except:
                if (check == 0):
                    engine.say("Please Say Again")
                    e.ask()
                elif (check == 1):
                    engine.say("Please Say Again")
                    e.to()
                elif (check == 2):
                    engine.say("Please Say Again")
                    e.send()
                elif (check == 3):
                    engine.say("Please Say Again")
                    e.conf()
                elif (check == 4):
                    e.talk("Please Say Again")
                    e.start()

            print(answer)
            return answer

    def send(self):
        msg = e.mic("Say The Subject", 2)
        print(msg)
        print(Email.to1)
        conform = e.mic("You Said " + msg + " Do you want to send or do you want to change", 2)
        if (conform == "send" or conform == "yes send" or conform == "yes"):
            print(Email.to1)
            server = sm.SMTP('smtp.gmail.com', 587)
            server.starttls()
            username=e.mic().lower().replace(" ","")
            password = e.mic().lower().replace(" ","")
            server.login(username, password)
            server.sendmail(username, Email.to1, msg)
            engine = py.init()
            engine.say("Mail Is Successfully Sent...")
            engine.runAndWait()
        elif (conform == "change" or conform == "chenge" or conform == "i want to change"):
            e.send()

    def conf(self):
        print("daliya")
        replay = e.mic("You Said " + Email.to1 + "Is this correct or wrong", 3)
        print(replay)
        if (replay == "correct" or replay == "yes" or replay == "s"):
            e.send()
        elif (replay == "wrong" or replay == "no"):
            e.to()
        else:
            e.talk("plaese Say Again")
            e.conf()

    # asking reciver email address
    def to(self):
        answer2 = e.mic("to whome you want to send", 1)
        temp = answer2.replace(" ", "")
        tomail = temp.lower()
        Email.to1 = tomail + "@gmail.com"
        print(Email.to1)

        e.conf()

    # 1
    def ask(self):
        answer = e.mic("You want send or read the mail", 0)
        if (answer == "sendmail" or answer == "send mail" or answer == "send" or answer == "send the mail"):
            check = 1
            e.to()

        elif (answer == "readmail" or answer == "read mail" or answer == "read"):
            e.talk(answer)
        else:
            e.talk("plaese Say Again")
            e.ask()



e = Email()
e.talk("Email System For Blinds")
e.ask()
