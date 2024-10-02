from transformers import MarianMTModel, MarianTokenizer

def download_model_and_tokenizer(model_name, local_dir):
    # Download the model and tokenizer and save them locally
    tokenizer = MarianTokenizer.from_pretrained(model_name, cache_dir=local_dir)
    model = MarianMTModel.from_pretrained(model_name, cache_dir=local_dir)
    return model, tokenizer

languages = ["de", "fr", "es", "ru"]

for lan in languages:
    # Specify the local directory to save the model and tokenizer
    local_model_dir = f"./models/opus-mt-en-{lan}"

    # Example usage: Download the English to German model and tokenizer
    model_name = f'{lan}'
    model, tokenizer = download_model_and_tokenizer(model_name, local_model_dir)
