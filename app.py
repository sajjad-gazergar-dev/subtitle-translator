# -----Imports----- #
from flask import Flask , request,redirect,url_for,render_template,send_file
from google import genai
import pysrt
from dotenv import load_dotenv
import re


# -----Setup----- #
load_dotenv()
app = Flask(__name__)


# -----Functions----- #
    
def translation(file):
    file = pysrt.open(file)
    numbered_list = []
    for i,e in enumerate(file, start=1) :
        numbered_list.append(f"{i}.{e.text}")
    prompt_body = "\n".join(numbered_list)
    client = genai.Client()
    interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=f"Translate each numbered line below into fluent Persian. Return the same numbers in the same order, one per line, nothing else:\n\n{prompt_body}"
    )
    result = interaction.output_text
    split_result = result.split("\n")
    parsed_result= []
    for i in split_result:
        parsed_result.append(i.split(".",1)[1])
    for entry,translation in zip(file,parsed_result):
        entry.text = translation
    file.save("translated.srt",encoding="utf_8")

# -----Routes----- #

@app.route("/",methods=["POST","GET"])

def index():
    if request.method == "POST":
        subtitle = request.files ['subtitle']
        if subtitle.filename.lower().endswith('.srt'):
            subtitle.save("temp.srt")
            translation('temp.srt')
        else:
            return render_template("index.html", error="Couldn't read that file — make sure it's a valid UTF-8 .srt")
        
        return send_file('translated.srt',as_attachment=True,download_name='translated.srt')
        
    return render_template('index.html')
    



# -----Main----- #
if __name__ == "__main__":
    app.run(debug=True)