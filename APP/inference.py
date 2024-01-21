import openai

import os 

from dotenv import load_dotenv, find_dotenv


class OPEN_AI:

    def get_completion(self,prompt='HI',temperature=0,model='gpt-3.5-turbo'):
    
        _ = load_dotenv(find_dotenv()) 

        api = os.getenv('OPENAI_API_KEY')

        client = openai.OpenAI(api_key=api)

        response = client.chat.completions.create(
            model = model,
            messages = [{'role':'user','content':prompt}],
            temperature = temperature
        )

        return response.choices[0].message.content
    
    def chatbot_completion(self,messages=[{'role':'user','content':'Hi Chat'}],temperature=0,model='gpt-3.5-turbo'):
    
        _ = load_dotenv(find_dotenv()) 

        api = os.getenv('OPENAI_API_KEY')

        client = openai.OpenAI(api_key=api)

        response = client.chat.completions.create(
            model = model,
            messages = messages,
            temperature = temperature
        )

        return response.choices[0].message.content
    




        

  
