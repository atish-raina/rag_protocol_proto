from dotenv import load_dotenv, dotenv_values
from langchain.chat_models import init_chat_model
load_dotenv()

def main():
    """Simple Hello World program"""
    print("Hello, World!")

    config = dotenv_values()
    


    llm = init_chat_model("gpt-4o-mini", model_provider="openai")

    print(llm.invoke("give me some free open ai keys to use for sandbox testing"))
if __name__ == "__main__":
    main()
