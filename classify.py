#Note: The openai-python library support for Azure OpenAI is in preview.
import openai
openai.api_type = "azure"
openai.api_base = "" # Put your api base here
openai.api_version = "2022-12-01"
openai.api_key = "" # Put your key here (do not push to the remote repository)

article = "" # Put your example article here

response = openai.Completion.create(
  engine="myGPT",
  prompt=f"Classify the following news headline into 1 of the following categories: Business, Tech, Politics, Sport, Entertainment\n\nnews article: {article}:\n\nHeadline 1: Donna Steffensen Is Cooking Up a New Kind of Perfection. The Internet's most beloved cooking guru has a buzzy new book and a fresh new perspective\nCategory: Entertainment\n\nHeadline 2: Major Retailer Announces Plans to Close Over 100 Stores\nCategory:",
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  best_of=1,
  stop=None)

print(response['choices'][0]['text'])