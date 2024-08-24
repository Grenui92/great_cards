This app was created because I learn English and I like to learn by using flashcards. But I can't find a good app for this.\
Somewhere I can't choose cards which I want to learn, somewhere I can't delete them from my collection.\
Stupid exercises, stupid algorithms... I hate it.\
So I try to write my app with Django.

You can start it like all Django projects with 
>python manage.py runserver

CHAT GPT
In .env you need to add your OpenAI API key, the app work with a free version of API.\
I try to configure GPT like an English teacher or something like this.

CHAT\
Bot talk with you in English and show you your mistakes in your sentences, answering your requests like an ordinary GPT.

In 'English sentences' you give your text to the bot, and he returns the correct text. 

CARDS
- You can create your own collections
- Create new cards and add them to the collection (cards saved in the Postgres, so if a card already exists it will get\
from DB if the card does not exist yet GPT will translate this word and add a new record to DB)
- For every card, GPT write interesting fact using words from this card (this is saved to DB too)\
I'm working on card sorting and checking answers (if correct - add the card to the end of the collection, if not - send\
the card for some positions lower). And I want to add voice acting by the neural network. 

And I see that I have bad code. Speaking of program code - my Django and Python learning is in progress.\
First - I want to rewrite all my views for Django built-in views. Next on the list is creating documentation and tests.
DOCUMENTATION https://grenui92.github.io/great_cards/