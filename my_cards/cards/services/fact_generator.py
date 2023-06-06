import openai

def fact_generator(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f'Write me an interesting fact about china using this word:\n\n {prompt}',
        temperature=0,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return response.choices[0].text.strip()
