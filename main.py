from fastapi import FastAPI
from googletrans import Translator


def translate_text(text, target_language='en'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text


app = FastAPI()

langcode = {"Hindi": "hi", "English": "en", "French": "fr", "German": "de", "Spanish": "es", "Italian": "it",
            "Japanese": "ja", "Korean": "ko", "Russian": "ru", "Chinese": "zh-cn"}
doc = {"message": "This is the documentation of the API",
       "/translate/{lang}/{name}": "This is the translation API. Enter the language and the text to be translated in the URL. For example, /translate/en/Hello will translate Hello to English. The language codes are as follows: Hindi: hi, English: en, French: fr, German: de, Spanish: es, Italian: it, Japanese: ja, Korean: ko, Russian: ru, Chinese: zh-cn"

       }
routes={
    "/":"Returns Hello World",
    "/translate/{lang}/{name}":"Returns the translated text. Enter the language and the text to be translated in the URL. For example, /translate/en/Hello will translate Hello to English. The language codes are as follows: Hindi: hi, English: en, French: fr, German: de, Spanish: es, Italian: it, Japanese: ja, Korean: ko, Russian: ru, Chinese: zh-cn",
    "/docapi":"Returns the documentation of the API",
    "/langcode":"Returns the language codes"
}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/translate/{lang}/{name}")
async def main(lang: str, name: str):
    translated_text = translate_text(name, target_language=lang)
    return {"message": f"{translated_text}"}


@app.get("/docapi")
async def docapi():
    return doc


@app.get("/langcode")
async def langcode():
    return langcode

