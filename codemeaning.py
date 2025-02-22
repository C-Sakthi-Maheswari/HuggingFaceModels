from transformers import AutoModel, AutoTokenizer

model_names = ["microsoft/codebert-base", "Salesforce/codet5-small", "bert-base-uncased"]
save_paths = ["local_models/codebert_base", "local_models/codet5_small", "local_models/bert_base_uncased"]

for model_name, path in zip(model_names, save_paths):
    model = AutoModel.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model.save_pretrained(path)
    tokenizer.save_pretrained(path)
    print(f"Saved {model_name} at {path}")
