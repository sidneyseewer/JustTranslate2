from transformers import MarianMTModel, MarianTokenizer
import os
from autoSpeaking import speak_text

def setup_tranlator(target_language):
    model_name = f'opus-mt-en-{target_language}'
    model_dir = f"models/opus-mt-en-{target_language}/snapshots"
    snapshot_dir = os.listdir(model_dir)[0]
    model_dir = f"{model_dir}/{snapshot_dir}"
    if not os.path.exists(model_dir):
        print("Path does not exist, exiting.")
        exit()
    # Load the tokenizer and model from the local directory
    tokenizer = MarianTokenizer.from_pretrained(model_dir)
    model = MarianMTModel.from_pretrained(model_dir)
    return tokenizer, model

def translate(text, target_language, tokenizer, model):
    # Tokenize the input text
    inputs = tokenizer.encode(text, return_tensors="pt")
    
    # Perform translation
    outputs = model.generate(inputs, num_beams=4, max_length=50, early_stopping=True)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return translated_text

def translate_continuous():
    tokenizer_de, model_de = setup_tranlator("de")
    tokenizer_fr, model_fr = setup_tranlator("fr")
    tokenizer_es, model_es = setup_tranlator("es")
    tokenizer_ru, model_ru = setup_tranlator("ru")
    tokenizers = [tokenizer_de, tokenizer_fr, tokenizer_es, tokenizer_ru]
    models = [model_de,model_fr,model_es,model_ru]
    languages = ['de', 'fr', 'es', 'ru']
    while(True):
        print("1: DE, 2: FR, 3: ES, 4: RU, 5: Quit")
        language = input("What language to tranlsate)")
        language = int(language)
        if language > 5 or language < 1:
            continue
        if language == 5:
            break
        while(True):
            text = input("Enter text to translate: ")
            if text == "":
                break
            translated_text = translate(text=text, target_language=languages[language-1],tokenizer=tokenizers[language-1],model=models[language-1])
            print(f"{languages[language-1]}: {translated_text}")
            # Speak output
            speak_text(text=translated_text, lan=languages[language-1])
    print("Good bye")

if __name__ == "__main__":
    translate_continuous()