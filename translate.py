# pip install translators
import translators as ts

text = 'আমি ভালো আছি।'
translated_text = ts.translate_text(text, translator='google', from_language='bn', to_language='en')
print(translated_text)