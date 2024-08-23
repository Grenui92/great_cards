import openai


def fact_generator(prompt):
    """Generate an interesting fact about Python using the given prompt.

    :param prompt: The word to be used in generating the fact.
    :return: The generated fact.
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
