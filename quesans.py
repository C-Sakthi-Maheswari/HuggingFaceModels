from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"

# Load the model and tokenizer
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

# Get user input
question = input("Enter your question: ")
context = input("Enter the context (paragraph containing the answer): ")

# Run the question-answering pipeline
QA_input = {'question': question, 'context': context}
res = nlp(QA_input)

# Display the result
print("\nAnswer:", res['answer'])
