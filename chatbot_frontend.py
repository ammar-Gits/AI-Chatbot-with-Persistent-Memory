import streamlit as st
import uuid
from chatbot_backend import chatbot, get_all_threads
from langchain.schema import HumanMessage, BaseMessage

# --------------------------
# Helper Functions
# --------------------------

def generate_thread_id():
    return str(uuid.uuid4())

def clear_chat():
    """Start a new chat thread."""
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    st.session_state['message_history'] = []
    add_thread(thread_id)

def add_thread(thread_id):
    """Add a thread to the list of threads if it doesn't exist."""
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    """Load the message history for a given thread from chatbot state."""
    state = chatbot.get_state(config={'configurable': {'thread_id': thread_id}})
    messages = state.values.get('messages', [])
    conversation = []
    for msg in messages:
        role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
        conversation.append({'role': role, 'content': msg.content})
    return conversation

# --------------------------
# Session State Initialization
# --------------------------

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = get_all_threads()


# --------------------------
# Sidebar UI
# --------------------------

st.sidebar.title("Chatbot")

if st.sidebar.button("New Chat"):
    clear_chat()

st.sidebar.title("My Conversations")
for thread_id in st.session_state['chat_threads']:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        st.session_state['message_history'] = load_conversation(thread_id)

# --------------------------
# Display Chat Messages
# --------------------------

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

# --------------------------
# User Input
# --------------------------

user_input = st.chat_input("Type your message here.")

if user_input:
    # Add user message to session state
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    # Prepare config for chatbot
    config = {'configurable': {'thread_id': st.session_state['thread_id']}}

    # Stream assistant response
    stream = chatbot.stream({'messages': [HumanMessage(content=user_input)]}, config=config, stream_mode='messages')

    with st.chat_message('assistant'):
        ai_message = st.write_stream(message_chunk.content for message_chunk, metadata in stream)

    # Save assistant response
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})
