import openai
from django.core.cache import cache

en = 'English'
ru = 'Russian'

def translator(text, from_l, to_l):

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate this from {from_l} into {to_l}:\n\n {text}",
        temperature=0.3,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0)

    return response['choices'][0].text




if __name__ == '__main__':
    print(translator('улица', from_l=ru, to_l=en))
