# -----Imports----- #
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.1-flash-lite",
    input="Explain how AI works in a few words"
)
print(interaction.output_text)