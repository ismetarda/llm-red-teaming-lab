from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
import warnings

# Suppress warnings for a cleaner terminal output
warnings.filterwarnings("ignore")

# Initialize the target LLM (e.g., TinyLlama) on the remote Host PC
llm = ChatOllama(model="tinyllama", base_url="http://192.168.1.9:11434")

print("💀 Basic Red Team Terminal Active! (Type 'q' or 'quit' to exit)")
print("-" * 60)

# Main interaction loop for basic Prompt Injection testing
while True:
    user_input = input("🥷 Payload (You): ")
    if user_input.lower() in ['q', 'quit', 'exit']:
        print("👋 Exiting framework...")
        break
    
    # Send the raw prompt to the model without any safety filters
    messages = [HumanMessage(content=user_input)]
    
    try:
        print("🤖 Target Model (Vulnerable): ", end="", flush=True)
        response = llm.invoke(messages)
        print(response.content)
        print("-" * 60)
    except Exception as e:
        print(f"\n❌ Connection error: {e}")
