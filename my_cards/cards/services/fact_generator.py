import openai

def fact_generator(prompt):
    """
    The fact_generator function takes a prompt as an argument and returns a fact about China.
    The function uses the OpenAI API to generate text using the &quot;text-davinci-003&quot; model, which is trained on Wikipedia articles.
    The function then returns the first choice of generated text from OpenAI's API.

    :param prompt: Pass in a word that the model will use to generate a fact about china
    :return: A string
    """

    messages = [{
     'role': 'system',
     'content': f'Write me an interesting fact about Python using this word:\n\n {prompt}. Use no more 100 chars.'   
    }]
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    return response.choices[0].message.content
