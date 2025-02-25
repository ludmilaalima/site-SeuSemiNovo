from dotenv import load_dotenv
import os
import openai

load_dotenv()


def get_car_description(model, brand, year):
    
    api_key = ''

    client = openai.OpenAI(
        base_url = "https://openrouter.ai/api/v1",
        api_key = os.getenv('API_KEY')
        
    )
    completion = client.chat.completions.create(
        model = 'deepseek/deepseek-r1:free',
        messages=[
            {'role': 'user', 
            'content': f"Faça uma descrição para um carro que tem seguintes características (no maximo 150 caracteres) marca: {brand},  modelo: {model}, ano: {year}"
            }
            
        ]
    )
    
    print("Resposta completa da API:", completion)
    return completion.choices[0].message.content







