from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage
import warnings

# Suppress deprecation warnings for cleaner console output
warnings.filterwarnings("ignore")

# Initialize the target LLM (Mistral) hosted on the remote machine
llm = ChatOllama(model="mistral", base_url="http://192.168.1.9:11434")

print("🔥 Red Team Terminal Active! (Type 'q' or 'quit' to exit)")
print("-" * 60)

# Interactive attack loop for manual Prompt Injection testing
while True:
    user_input = input("🥷 Payload (You): ")
    if user_input.lower() in ['q', 'quit', 'exit']:
        print("👋 Terminating connection...")
        break
    
    # Send the raw, malicious prompt directly to the unprotected model
    messages = [HumanMessage(content=user_input)]
    
    try:
        print("🤖 Mistral (Vulnerable): ", end="", flush=True)
        response = llm.invoke(messages)
        print(response.content)
        print("-" * 60)
    except Exception as e:
        print(f"\n❌ Connection error (Is Ollama running?): {e}")
