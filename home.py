# prompt: write a code for creating the AI-powered mental health chatbot

# Install necessary libraries
!pip install transformers

# Import libraries
from transformers import pipeline

# Create a text generation pipeline using a pre-trained model
# You can replace 'gpt2' with other models like 'microsoft/DialoGPT-medium' for better performance
# but be aware of the increased resource usage
classifier = pipeline("text-generation", model="gpt2")

def get_bot_response(user_input):
  """Generates a response from the chatbot based on user input."""
  response = classifier(user_input, max_length=50, num_return_sequences=1)
  return response[0]['generated_text']


def main():
  """Main function to run the chatbot."""
  print("Welcome to the AI Mental Health Chatbot!")
  print("Type 'quit' to exit.")

  while True:
      user_input = input("You: ")
      if user_input.lower() == "quit":
          break

      bot_response = get_bot_response(user_input)
      print("Bot:", bot_response)

if __name__ == "__main__":
    main()
