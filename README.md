# RAG Protocol Prototype

A prototype project for experimenting with Retrieval-Augmented Generation (RAG) protocols.

---

## Installation

First, create and activate a new virtual environment:

```bash
python -m venv rag_env
source rag_env/bin/activate
```

Then, install the required dependencies:

```bash
pip install --upgrade langchain-text-splitters langchain-community langgraph
```

---

## Package Descriptions

- **langchain-text-splitters**: Split text documents into smaller chunks for processing.
- **langchain-community**: Community package for LangChain, providing integrations and tools.
- **langgraph**: Used to create agent systems and workflows.

---

## Usage

After installing dependencies, you can run your Python scripts as usual:

```bash
python main.py
```

---

## Notes

- Always activate your virtual environment before installing packages or running scripts.
- Do **not** commit your `rag_env/` folder to version control. Use a `.gitignore` file to exclude it.

---

## License

[MIT License](LICENSE)