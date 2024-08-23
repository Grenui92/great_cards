import openai


def chekicg_sentences(prompt):
    """The text_generator function takes a string as an argument and returns the
    same string with any spelling errors corrected.

    :param prompt: Pass the text that needs to be corrected
    :return: The corrected text
    """
    messages = [{
        'role': 'system',
        'content': f'Fix the mistakes in this sentence or rewrite it in proper\
         English: {prompt}. Then translate the text into Russian and write it\
         in brackets'
    }]

    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )

    return response.choices[0].message.content
