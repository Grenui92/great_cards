import openai

def text_generator(prompt):
    """
    The text_generator function takes a string as an argument and returns the same string with any spelling errors corrected.

    :param prompt: Pass the text that needs to be corrected
    :return: The corrected text
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Correct this to standard English:\n\n {prompt}',
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].text

