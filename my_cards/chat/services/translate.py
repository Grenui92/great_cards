import openai


def translate_ru_en(prompt):
    language = 'English'
    return translate(language=language, prompt=prompt)


def translate_en_ru(prompt):
    language = 'Russian'
    return translate(language=language, prompt=prompt)


def translate(language, prompt):
    """
    The text_generator function takes a string as an argument and returns the
    same string with any spelling errors corrected.

    :param prompt: Pass the text that needs to be corrected
    :return: The corrected text
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
