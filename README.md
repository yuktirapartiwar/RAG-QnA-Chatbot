# RAG-QnA-Chatbot

## Description
RAG-QnA-Chatbot is a conversational AI chatbot built using Flask and OpenAI's GPT-3.5 model. Users can upload a PDF document which the chatbot will reference to answer queries. The application ensures that responses are contextual, leveraging the conversation history to provide accurate and relevant answers. This project showcases how advanced natural language processing techniques can be integrated into a web application to provide a seamless user experience.

The application flow involves:

- **Uploading a PDF Document:** Users can upload a PDF document that they want the chatbot to reference.
- **User Query:** Users can type in their questions in the chat interface.
- **Retrieval-Augmented Generation:** The chatbot uses RAG techniques to retrieve relevant information from the uploaded PDF and generate a coherent response.
- **Maintaining Conversation History:** The chatbot keeps track of the conversation to provide contextual responses.

## Skills and Technologies Used
**Frontend**
- **HTML:** The structure of the web pages is defined using HTML.
- **CSS:* Custom styles for the chatbot interface.
- **Bootstrap:** Utilized for responsive design and pre-styled components, making the UI aesthetically pleasing and user-friendly.

**Backend**
- **Python:** Used for backend development, including implementing the Flask web framework and integrating with the OpenAI API.
- **Flask:** Used as the web framework to build the chatbot application. Flask handles routing, form submissions, and session management.
- **UUID:** Used for generating unique session IDs to maintain user sessions.
- **PyPDFLoader:** Loads and processes PDF documents.
- **dotenv:** Used for loading environment variables, ensuring secure and configurable settings.

- **OpenAI API GPT-3.5 Model:** Utilized for natural language processing and generating AI-powered responses.
- **LangChain:** A framework for building conversational AI systems, providing tools for document handling, retrieval, and generation.
- **OpenAIEmbeddings:** Embeddings are used to represent the text data in a format suitable for retrieval and generation tasks.
- **RecursiveCharacterTextSplitter:** Splits the documents into manageable chunks for processing.
- **ChromaDB:** A vector store used for indexing and retrieving contextual information from documents.
- **History-Aware Retriever:** Keeps track of the conversation history to provide contextual question reformulation.

## Features
- **User-Friendly Interface:** The chatbot interface is designed to be intuitive and easy to use, with a clean layout and responsive design.
- **PDF Document Upload:** Users can upload PDF documents which the chatbot will use as a reference to answer questions.
- **Contextual Responses:** The chatbot leverages conversation history to provide accurate and contextually relevant answers using RAG.
- **Secure File Handling:** Ensures that uploaded files are securely handled and stored.
- **Session Management:** Each user session is tracked to maintain a seamless conversation experience.
- **Responsive Design:** Built using Bootstrap, the application is responsive and works well on various devices, including desktops, tablets, and mobile phones.

