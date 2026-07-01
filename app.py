# -----Imports----- #
from flask import Flask , request,redirect,url_for,render_template,send_file
from google import genai
import pysrt
from dotenv import load_dotenv


# -----Setup----- #
load_dotenv()
app = Flask(__name__)


# -----Functions----- #
    
def translate(file):
    file = pysrt.open(file)
    client = genai.Client()

    for i in file:

        interaction = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input=f"Translate the given text into fluent persian and only output the translation nothing else: {i.text}"
        )
        i.text = interaction.output_text
        
    file.save("translated.srt",encoding='utf_8')
# -----Routes----- #

@app.route("/",methods=["POST","GET"])

def index():
    sub_text = None
    if request.method == "POST":
        subtitle = request.files ['subtitle']
        subtitle.save("temp.srt")
        translate("temp.srt")
        return send_file('translated.srt',as_attachment=True,download_name='translated.srt')
    return render_template('index.html')
    



# -----Main----- #
if __name__ == "__main__":
    app.run(debug=True)