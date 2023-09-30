import os
import webbrowser
import file_handling as fh
import features as f
import chatbot as cb
from AppOpener import open, close


def main():
    f.wishMe()

    check_file = os.path.isfile('./database/history.txt')
    if not check_file: 
        fh.create_file("./database/history.txt")
   
    
    
                
    while True:
        query = f.takeCommand().lower()
        fh.append_data("./database/history.txt", "USER", query)

        #logic for executing commands
        if 'wikipedia' in query:
            f.wikiPedia(query)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            fh.append_data("./database/history.txt", "VOICY","youtube opened")

        elif 'open google' in query:
            webbrowser.open("google.com")
            fh.append_data("./database/history.txt", "VOICY","google opened")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
            fh.append_data("./database/history.txt", "VOICY","facebook opened")

        elif 'open amazon' in query:
            webbrowser.open("amazon.com")
            fh.append_data("./database/history.txt", "VOICY","amazon opened")

        elif 'open flipkart' in query:
            webbrowser.open("flipkart.com")
            fh.append_data("./database/history.txt", "VOICY","flipkart opened")

        elif 'open excel' in query:
            open('excel')
            fh.append_data("./database/history.txt", "VOICY","excel closed")

        elif 'close excel' in query:
            close('excel')
            fh.append_data("./database/history.txt", "VOICY","excel closed")

        elif 'open notepad' in query:
            open('notepad')
            fh.append_data("./database/history.txt", "VOICY","notepad opened")

        elif 'close notepad' in query:
            close('notepad')
            fh.append_data("./database/history.txt", "VOICY","notepad closed")

        elif 'time' in query:
            f.time()
    
        elif 'date' in query:
            f.date()

        elif 'chat' in query:
            cb.chatBot()

        elif 'sleep' in query:
            fh.append_data("./database/history.txt", "VOICY","Thank You!!!")
            f.speak("Thank You")
            break;
        
        elif 'clear history' in query:
            fh.delete_file("./database/history.txt")
        
        elif 'how are you' in query:
            f.speak("I am fine sir")
            fh.append_data("./database/history.txt", "VOICY", "I am fine sir")