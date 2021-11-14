import requests
import os
import shutil
from gtts import gTTS

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
}

os.chdir("main/static/main")


def pic_download(USER_ID):
    INSTA_URL = "https://www.instagram.com/"
    TAIL = "/?__a=1"

    URL = INSTA_URL + USER_ID + TAIL

    response = requests.get(URL, headers=header).json()

    hd_image_location = response["graphql"]["user"]["profile_pic_url_hd"]
    hd_image_response = requests.get(hd_image_location, stream=True)

    if os.path.isfile("1.jpg"):
        os.remove("1.jpg")
    with open("1.jpg", "wb") as out_file:
        shutil.copyfileobj(hd_image_response.raw, out_file)


def ttss(t, l):
    tts = gTTS(t, lang=l)
    if os.path.isfile("aud.wav"):
        os.remove("aud.wav")
    tts.save("aud.wav")


langs = [
    {
        "af": "Afrikaans",
        "ar": "Arabic",
        "bn": "Bengali",
        "bs": "Bosnian",
        "ca": "Catalan",
        "cs": "Czech",
        "cy": "Welsh",
        "da": "Danish",
        "de": "German",
        "el": "Greek",
        "en": "English",
        "eo": "Esperanto",
        "es": "Spanish",
        "et": "Estonian",
        "fi": "Finnish",
        "fr": "French",
        "gu": "Gujarati",
        "hi": "Hindi",
        "hr": "Croatian",
        "hu": "Hungarian",
        "hy": "Armenian",
        "id": "Indonesian",
        "is": "Icelandic",
        "it": "Italian",
        "ja": "Japanese",
        "jw": "Javanese",
        "km": "Khmer",
        "kn": "Kannada",
        "ko": "Korean",
        "la": "Latin",
        "lv": "Latvian",
        "mk": "Macedonian",
        "ml": "Malayalam",
        "mr": "Marathi",
        "my": "Myanmar",
        "ne": "Nepali",
        "nl": "Dutch",
        "no": "Norwegian",
        "pl": "Polish",
        "pt": "Portuguese",
        "ro": "Romanian",
        "ru": "Russian",
        "si": "Sinhala",
        "sk": "Slovak",
        "sq": "Albanian",
        "sr": "Serbian",
        "su": "Sundanese",
        "sv": "Swedish",
        "sw": "Swahili",
        "ta": "Tamil",
        "te": "Telugu",
        "th": "Thai",
        "tl": "Filipino",
        "tr": "Turkish",
        "uk": "Ukrainian",
        "ur": "Urdu",
        "vi": "Vietnamese",
        "zh-CN": "Chinese"
    }
]
