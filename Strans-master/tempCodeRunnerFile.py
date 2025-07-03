from flask import Flask, render_template, request
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        lang = request.form.get("lang", "en")

        # where to put your TTS file in the static folder
        mp3_path = os.path.join(app.static_folder, "translated_output.mp3")

        # delete any existing file so we can overwrite
        if os.path.exists(mp3_path):
            os.remove(mp3_path)

        # perform the translation
        translated_text = translator.translate(text, dest=lang).text

        # generate and save the new MP3
        tts = gTTS(translated_text, lang=lang)
        tts.save(mp3_path)

    return render_template("index.html",
                           translated_text=translated_text)


if __name__ == "__main__":
    app.run(debug=True)
