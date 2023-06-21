import openai

en = 'English'
ru = 'Russian'

def translator(text, from_l, to_l):
    """
    The translator function takes in a string of text, the language it is currently written in, and the language to translate
    it into. It then uses OpenAI's API to generate a translation of that text. The function returns this translated text.

    :param text: Pass the text to be translated
    :param from_l: Specify the language that the text is currently in
    :param to_l: Specify the language to translate into
    :return: A string
    """
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
