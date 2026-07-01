# Building a sutitle translator using ai 

### we write a web app which with ai (e.g. gemini) translate the subtitle to persian 

### Input
- file.srt
### Output 
-translated_file.srt 


## Gemini API guide :
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.5-flash",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)




## Plan
we need to find out how to take file with python , it has to be only srt 
and we need to be able to read srt file and seperate the text then save it , translate it and build a new file with old timestamp but with new text 

first we test how to read a srt file 
- there is a library called pysrt
- update : i have access to only text part 
#### Libraries 
- for working with files we use python own with open 
- gemini sdk 







