# LangChain Agent

A simple conversational AI agent built with LangChain and LangGraph that can perform basic arithmetic operations and engage in natural language conversations.

## Features

- **Interactive Chat Interface**: Continuous conversation loop with the AI agent
- **Calculator Tool**: Performs basic arithmetic operations (addition, subtraction, multiplication, division)
- **Weather Info Tool**: Gets the information about weather in different cities around the world
- **OpenAI Integration**: Uses OpenAI's GPT models for natural language understanding
- **Tool Integration**: Demonstrates how to create and integrate custom tools with LangChain agents

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Openweather API key

## Installation

1. **Clone or download the code**

2. **Install required packages**:
   ```bash
   pip install langchain langchain-openai langgraph python-dotenv
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project directory and add your OpenAI and Openweather API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   OPENWEATHER_API_KEY=your_openweather_api_key_here
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Interact with the agent**:
   - The agent will greet you and explain its capabilities
   - Type your questions or requests
   - Ask for calculations like "What's 15 + 25?" or "Calculate 100 divided by 4"
   - Ask for weather of cities around the world.
   - Have general conversations
   - Type `quit` to exit
