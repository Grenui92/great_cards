import openai

en = 'English'
ru = 'Russian'

def translator(text, from_l, to_l):
    """
    The translator function takes in a string of text, the language it is currently written in, and the language to translate
    it into. It then uses OpenAI's API to generate a translation of that text. The function returns this translated text.

    :param text: Pass the text to be translated
    :param from_l: Specify the language that the text is currently in
    :param to_l: Specify the language to translate into
    :return: A string
    """


    messages = [{
     'role': 'system',
     'content': f"Translate this from {from_l} into {to_l}:\n\n {text}"   
    }]
    
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    return response.choices[0].message.content

