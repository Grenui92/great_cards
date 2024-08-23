import openai

en = 'English'
ru = 'Russian'


def translator(text, from_l, to_l):
    """Translate text from one language to another.

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
