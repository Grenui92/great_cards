from cards.models import EnglishCards
from cards.services.collections_services import CollectionSrvices
from cards.services.translator import translator, en, ru
from cards.services.fact_generator import fact_generator
import logging


class CardsServices:
    @classmethod
    def get_information_from_forms(cls, form):
        """Return three attrs in this order
        english_word: str
        russian_word: str
        word_usage: str
        collection: CardsCollection object"""

        english_word = form.cleaned_data['english_word']
        russian_word = form.cleaned_data['russian_word']
        word_usage = form.cleaned_data['word_usage']
        collection = CollectionSrvices.get_collection_by_id(collection_id=form.cleaned_data['collection'])
        return english_word, russian_word, word_usage, collection

    @staticmethod
    def generate_data(english_word, russian_word, word_usage):

        if not english_word:
            english_word = translator(text=russian_word, from_l=ru, to_l=en).strip()

        elif not russian_word:
            russian_word = translator(text=english_word, from_l=en, to_l=ru).strip()

        if not word_usage:
            word_usage = fact_generator(english_word).strip()

        return english_word, russian_word, word_usage

    @classmethod
    def get_card_from_collection(cls, english, russian):
        if english:
            card = EnglishCards.objects.get(english_word=english)
        elif russian:
            card = EnglishCards.objects.get(russian_word=russian)
        else:
            raise ValueError('Empty fields "english word" or "russian word"')
        return card

    @classmethod
    def get_new_card(cls, form):
        english, russian, usage, collection = cls.get_information_from_forms(form)
        try:

            card = cls.get_card_from_collection(english=english, russian=russian)
            collection.cards.add(card)

            # Если не нашли - сохранем форму в БД
        except EnglishCards.DoesNotExist as exc:

            logging.info(exc)
            english_word, russian_word, word_usage = cls.generate_data(english, russian, usage)

            card = EnglishCards.objects.create(english_word=english_word,
                                               russian_word=russian_word,
                                               word_usage=word_usage)
            collection.cards.add(card)

        except Exception as exc:

            logging.info(exc)
            return {'message': f'Something goes wrong!!!\n {exc}'}

        # Уведомление об спешном создании(нахождение существующей) карточки и добавлении ее в выбраную коллекцию
        logging.info(f'Success')
        return {'message': f'Card "{english}" successfully created and added to the collection "{collection.name}"'}
