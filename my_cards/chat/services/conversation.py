import openai


def chat_bot(messages):
    """The text_generator function takes in a list of messages and returns the
    role (speaker) and content (message) of the first response from OpenAI's
    GPT-3 API. The function is used to generate responses to user input.

    :param messages: A list of messages that the chatbot has received,\
    including the user's input.
    :return: A tuple of the role and content
    """
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=messages
    )
    return response.choices[0].message.role, response.choices[0].message.content
