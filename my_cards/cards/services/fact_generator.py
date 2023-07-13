import openai

def fact_generator(prompt):
    """
    The fact_generator function takes a prompt as an argument and returns a fact about China.
    The function uses the OpenAI API to generate text using the &quot;text-davinci-003&quot; model, which is trained on Wikipedia articles.
    The function then returns the first choice of generated text from OpenAI's API.

    :param prompt: Pass in a word that the model will use to generate a fact about china
    :return: A string
    """
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Write me an interesting fact about Python using this word:\n\n {prompt}',
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].text.strip()
