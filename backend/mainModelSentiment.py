from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline

# Using Fine Tuned FineBERT (FinBERT-tone)
# Which achieves superior performance on financial tone analysis task
def instantitateModelSentiment():
    finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
    tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
    model = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)
    return model