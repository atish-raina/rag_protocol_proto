from dotenv import load_dotenv, find_dotenv, dotenv_values

load_dotenv()

def main():
    """Simple Hello World program"""
    print("Hello, World!")

    config = dotenv_values()
    
    print(f"\nLangSmith Configuration:")
    print(f"Tracing enabled: {config.get('LANGSMITH_TRACING', 'Not set')}")
    print(f"API Key configured: {'Yes' if config.get('LANGSMITH_API_KEY') else 'No'}")


if __name__ == "__main__":
    main()
