# Multi Agent Chatbot 

An AI-powered chatbot that maintains **persistent chat histories** and supports **multiple conversation threads**. Built with **LangGraph** and **LangChain**, it uses **HuggingFace LLaMA-3.2-1B** for natural language understanding and response generation, **Streamlit** for the frontend, and **SQLite** for storing chat states. The system is future-ready for **RAG (Retrieval-Augmented Generation)** to provide knowledge-based responses.

---

## Features

- **Persistent Conversations:** Save and resume chats across sessions with SQLite.  
- **Multiple Threads:** Start new chats or switch between existing threads seamlessly.  
- **AI-Powered Responses:** HuggingFace LLaMA-3.2-1B handles natural language understanding and generation.  
- **Interactive Frontend:** Streamlit UI with real-time streaming of assistant responses.  
- **Future RAG Integration:** Plans to retrieve information from external knowledge sources for more informed answers.  

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-chatbot.git
   cd ai-chatbot
