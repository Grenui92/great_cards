import openai

def text_generator(messages):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    return response.choices[0].message.role, response.choices[0].message.content

