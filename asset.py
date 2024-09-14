from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Define the chat template
template = """
Answer the question based on the conversation history.

Conversation history:
{context}

Question: {question}

Answer:
"""

# Initialize the Ollama language model
model = OllamaLLM(model="llama3.1")

# Create a chat prompt template
prompt = ChatPromptTemplate.from_template(template)

# Create a chain that combines the prompt and the model
chain = prompt | model

def handle_conversation():
    # Initialize an empty context to store conversation history
    context = ""
    print("Welcome to the AI chatbot")
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if the user wants to exit
        if user_input.lower() == "exit":
            break
        
        # Generate a response using the language model
        result = chain.invoke({"context": context, "question": user_input})
        
        # Print the AI's response
        print("Bot:", result)
        
        # Update the context with the new interaction
        context += f"\nUser: {user_input}\nAI: {result}"

# Check if this script is being run directly
if __name__ == "__main__":
    handle_conversation()