from machinetranslation import translator
from machinetranslation.translator import english_to_french, french_to_english

from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench", methods=["GET"])
def englishToFrench():
    textToTranslate = request.args.get("textToTranslate")
    translatedText = english_to_french(textToTranslate)
    # Write your code here
    return translatedText

@app.route("/frenchToEnglish", methods=["GET"])
def frenchToEnglish():
    textToTranslate = request.args.get("textToTranslate")
    translatedText = french_to_english(textToTranslate)
    # Write your code here
    return translatedText

@app.route("/")
def render_index_page():
    # Write the code to render template
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
