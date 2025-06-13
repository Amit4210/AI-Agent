import os
import requests
import json
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float) -> str:
    '''Used to perform basic arithmetic operations with numbers.'''
    return f'The sum of {a} and {b} is {a+b}.'

@tool
def weather_info(city: str) -> str:
    ''' Get the weather information for a city. Requires the openweather API key. '''
    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        print('API key not found. Add OPENWEATHER_API_KEY to your .env file. ')

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url) ##
        data = response.json() ##

        if response.status_code == 200: ##
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']
            return f'Weather in {city}:{temp}°C, {description}, humidity: {humidity}%'
        else:
            return f"Could not get weather for {city}: {data.get('message', 'Unknown error')}"
    except Exception as e:
        return f"Error getting weather: {str(e)}"






def main():
    model = ChatOpenAI(temperature=0)

    tools = [calculator, weather_info]
    agent_executor = create_react_agent(model, tools)

    print('Welcome! This is your AI Agent. Press \'quit\' to exit.')
    print('You can chat with me or ask me to perform calculations or ask me about the weather,')

    while True:
        user_input = input('\nYou: ').strip()

        if user_input.lower() == 'quit':
            print('Thank You.')
            break
        print('\n🤖Assistant: ', end='')
        for chunk in agent_executor.stream(
                {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content,end='')

        print()

if __name__ == "__main__":
    main()
