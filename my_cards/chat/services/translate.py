import openai

def translate_ru_en(prompt):
    language = 'English'
    return translate(language=language, prompt=prompt)

def translate_en_ru(prompt):
    language = 'Russian'
    return translate(language=language, prompt=prompt)
def translate(language, prompt):
    """
    The text_generator function takes a string as an argument and returns the same string with any spelling errors corrected.

    :param prompt: Pass the text that needs to be corrected
    :return: The corrected text
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Translate to {language}:\n\n {prompt}',
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].text