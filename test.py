import env
import pyttsx3
import wolframalpha
import wikipedia
import ssl
app_id = env.appid
try:
        _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
# Legacy Python that doesn't verify HTTPS certificates by default
        pass
else:
# Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
# ssl.create_default_context = ssl._create_unverified_context
client = wolframalpha.Client(app_id)
res = client.query("capital of india")
wolfram_res = next(res.results).text
engine = pyttsx3.init()
engine.say(""+wolfram_res)
engine.runAndWait()