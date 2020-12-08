import wolframalpha
import ssl
import wikipedia
import PySimpleGUI as sg
import pyttsx3
import env

app_id = env.appid  # get your own at https://products.wolframalpha.com/api/
ssl._create_default_https_context = ssl._create_unverified_context
client = wolframalpha.Client(app_id)

sg.theme('DarkPurple')

layout = [[sg.Text('Enter a command'), sg.InputText()], 
        [sg.Button('Ok'), sg.Button('Cancel')]]

window = sg.Window('PyDa', layout)

while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Cancel':
                break
        engine = pyttsx3.init()
        try:
                wiki_res = wikipedia.summary(values[0], sentences=2)
                res = client.query(values[0])
                wolfram_res = next(res.results).text
                engine.say(wolfram_res)
                engine.runAndWait()
                sg.PopupNonBlocking("Wolfram result: "+wolfram_res, "Wikiepedia result: "+wiki_res)
        except wikipedia.exceptions.DisambiguationError:
                res = client.query(values[0])
                wolfram_res = next(res.results).text
                engine.say(wolfram_res)
                engine.runAndWait()
                sg.PopupNonBlocking(wolfram_res)
        except wikipedia.exceptions.PageError:
                wolfram_res = next(client.query(values[0]).results).text
                engine.say(wolfram_res)
                engine.runAndWait()
                sg.PopupNonBlocking(wolfram_res)
        except:
                wiki_res = wikipedia.summary(values[0], sentences=2)
                engine.say(wiki_res)
                engine.runAndWait()
                sg.PopupNonBlocking(wiki_res)

window.close()