from num2words import num2words
import googletrans

num = int(input("Enter the number you want to convert into words : "))

print(f"\n{googletrans.LANGUAGES}\n")
language = input("Select any language above to convert in it : ")

words_eng = num2words(num)

for i in googletrans.LANGUAGES.keys():

    if (language.lower()==i):
        translator = googletrans.Translator()
        words_lang = translator.translate(words_eng, language.lower(), 'en').text
        break

    else:
        words_lang = "Please select a language"


print("In Numbers : ", num)
print("In Words : ", words_lang)
