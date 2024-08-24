from cards.models import Cards
from cards.services.collections_services import CollectionServices
from cards.services.translator import translator, en, ru
from cards.services.fact_generator import fact_generator

import logging


class CardsServices:
    """The CardsServices class provides methods for interacting with cards."""

    @classmethod
    def get_information_from_forms(cls, request):
        """Takes in a request object and returns the values of the form fields.

        :param cls: Refer to the class itself
        :return: A tuple of four values
        """
        english_word = request.GET['english_word']
        russian_word = request.GET['russian_word']
        word_usage = request.GET['word_usage']
        collection = CollectionServices.get_collection_by_id(
            collection_id=request.GET['collection_choice'])
        return english_word, russian_word, word_usage, collection

    @classmethod
    def get_card_data(cls, english_word, russian_word, word_usage):
        """This function gets the Card from the database and returns a tuple of
        three values.
        If the user does not provide an English word or a Russian word,
        the function will use translator() to translate the provided
        language into the other language.
        If no usage is provided by the user, then it will be generated using
        the fact generator function.

        :param cls: Refer to the class itself
        :param english_word: Pass the english word to the function
        :param russian_word: Pass the russian word to the function
        :param word_usage: Pass a fact about the word to the function
        :return: A tuple of three values.
        """
        try:
            card: Cards = cls.get_card_from_collection(
                english=english_word, russian=russian_word)
            return card.english_word, card.russian_word, card.word_usage

        except Cards.DoesNotExist:
            if not english_word:
                english_word = translator(
                    text=russian_word, from_l=ru, to_l=en).strip()

            elif not russian_word:
                russian_word = translator(
                    text=english_word, from_l=en, to_l=ru).strip()

            if not word_usage:
                word_usage = fact_generator(english_word).strip()

            return english_word.lower(), russian_word.lower(), word_usage.lower()

    @classmethod
    def get_card_from_collection(cls,
                                 english=None,
                                 russian=None,
                                 card_id=None):
        """Takes in a string of either an English word or Russian word, and
        returns the corresponding card object from the database.
        If no such card exists, it raises a ValueError.

        :param cls: Refer to the class itself
        :param english: Get the card from the database using its english word,\
        default is None
        :param russian: Get the card from the database, default is None
        :param card_id: Get a card by its id, default is None
        :return: A Card instance from the database
        :raises: ValueError if no card is found
        """
        if english:
            card = Cards.objects.get(english_word=english)
        elif russian:
            card = Cards.objects.get(russian_word=russian)
        elif card_id:
            card = Cards.objects.get(id=card_id)
        else:
            raise ValueError('Empty fields "english word" and "russian word"')

        return card

    @classmethod
    def get_new_card(cls, english, russian, usage, collection):
        """Get the information from the parameters and create a new card
        in the database. If the card already exists, it will be added to the
        collection.

        :param cls: Refer to the class itself
        :param form: Get the information from the form
        :return: A dictionary with a message
        """
        try:
            card = cls.get_card_from_collection(
                english=english, russian=russian)
            collection.cards.add(card)

        except Cards.DoesNotExist as exc:
            logging.info(exc)
            card = Cards.objects.create(english_word=english,
                                        russian_word=russian,
                                        word_usage=usage)
            collection.cards.add(card)

        except Exception as exc:
            return {'message': f'Something goes wrong!!!\n {exc}'}

        if card.id not in collection.order_list:
            collection.order_list.insert(0, card.id)
            collection.save()

        return card
