import openai
import features as f
import file_handling as fh


openai.api_key = "enter your your api key"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

def chatBot():
    f.speak("Hello I am you personal ChatBot")
    fh.append_data("./database/history.txt", "VOICY","Hello I am you personal ChatBot \n")

    while(True):
        text = f.takeCommand()
        fh.append_data("./database/history.txt", "USER", text)
        if(text == "stop"):
            f.speak("Thank You, Nice to meet you.")
            break

        else:
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
            )

        f.speak(response["choices"][0]["text"])
        text = response["choices"][0]["text"]
        print(text)
        fh.append_data("./database/history.txt", "VOICY", text)