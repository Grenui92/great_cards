# Great Cards

Site [dontlosehope.website](dontlosehope.website)\
Documentation [docs](https://grenui92.github.io/great_cards/)\
Technologies used:
- Python ^3.10
- Django ^4.2.1
- Django Channels ^4.0.0
- Daphne ^4.0.0
- Redis ^4.5.5
- Celery ^5.3.6
- Postgresql from [elephantsql.com](elephantsql.com)

The primary purpose of creating this application was to assist myself in learning English. I felt the need for interaction with subtitles on YouTube (interactive translation of highlighted text fragments), more comprehensive interaction with flashcards for learning words (creating collections of flashcards, setting reminder frequencies independently), and a lack of a teacher to guide me on how to construct sentences correctly in English and to identify my errors. 

## Functionality

### News

Here will appear news in English, but with the option to translate text when highlighted and add the highlighted text to flashcard collections for memorization.
Unfortunately, this part of the functionality is not yet implemented, as I have not been able to find a free accessible API for interacting with news in the topic of interest to me and adding them to the website.

### Cards

Those are the flashcards for learning words. You can create an unlimited number of collections, add an unlimited number of cards. When studying the cards, clicking "I know it" sends the card to the end of the collection, clicking "Remind" moves it by 4 positions (a reminder for yourself – to make this function customizable for a shift from 4 to 20 cards).

Also, when creating a card, an interesting fact about Python in English is generated using the added word, but this function is ***experimental*** as instructions for ChatGPT need improvement and new versions available via the API need to be tested.

### GPT

#### Sentences
Simply functionality – you provide the chat with a sentence in English, and it, to the best of its ability and understanding, tries to correct your mistakes and returns the corrected sentence to you.
#### Chat with GPT-3
Regular chat with ChatGPT, but its main feature is that it tries to explain your mistakes. It is preferable to write to it in English, it will correct the grammar of the question and try to provide an answer.
#### To Russian / To English
Translation of text to Russian / to English with proposed translation options.

### Times

List of English language tenses, with a brief description of the essence of each tense, a schematic sentence structure, and examples of complete sentences (affirmative, negative, question).

### Tube

Interacting with YouTube videos and their subtitles. By adding a video in the "Upload video from YT" tab, you insert a link from YouTube and after a short time (usually less than 10 seconds), the video will be added to your list of videos. The viewing itself happens through the iframe_api. Subtitles are also displayed in a separate window, where you can select them, translate the selected text, and save it on cards for learning.
