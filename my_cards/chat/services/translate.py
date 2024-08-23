import openai


def translate_ru_en(prompt):
    """Translate the text from Russian to English.

    :param prompt: The text that needs to be translated
    :return: The translated text
    """
    language = 'English'
    return translate(language=language, prompt=prompt)


def translate_en_ru(prompt):
    """Translate the text from English to Russian.

    :param prompt: The text that needs to be translated
    :return: The translated text
    """
    language = 'Russian'
    return translate(language=language, prompt=prompt)


def translate(language, prompt):
    """Translate the text from one language to another.

    :param language: The language to which the text should be translated
    :param prompt: The text that needs to be translated
    :return: The translated text
    """
    messages = [{
        'role': 'system',
        'content': f'Translate to {language}:\n\n {prompt}.'
        'Offer different translation options, each option starting with *.'
    }]

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    return response.choices[0].message.content
