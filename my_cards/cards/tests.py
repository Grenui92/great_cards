from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from cards.models import Collections, Cards
from cards.forms import CardForm
from cards.views.collection_views import CollectionListView
from cards.views.card_views import CardsListView


class CardsStaticTestCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user_1 = User.objects.create(username='TestUser_1', email='test@test.test')
        cls.collection_u1_c1 = Collections.objects.create(name='Test_1', owner=cls.user_1)
        cls.collection_u1_c2 = Collections.objects.create(name='Test_2', owner=cls.user_1)

        cls.user_2 = User.objects.create(username='TestUser_2', email='test@test.test')
        cls.collection_u2_c1 = Collections.objects.create(name='Test_3', owner=cls.user_2)
        cls.collection_u2_c2 = Collections.objects.create(name='Test_4', owner=cls.user_2)

        cls.cards = [Cards.objects.create(english_word=f'english_test_{n}',
                                          russian_word=f'russian_word_{n}',
                                          word_usage=f'test_usage_{n}') for n in range(3)]

        cls.collection_u1_c1.cards.add(*cls.cards)

        cls.request_factory = RequestFactory()


    def test_url_study_cards(self):
        url = reverse('cards:study_cards')
        self.client.force_login(self.user_2)

        # Check status code
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


        # Check list of user-owned collections
        collections_list = list(response.context_data['object_list'])
        self.assertListEqual(list(collections_list), [self.collection_u2_c1, self.collection_u2_c2])

    def test_url_open_collection(self):
        url = reverse('cards:open_collection', kwargs={'collection_id': self.collection_u1_c1.id})

        #Check status code
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

        #Check that paginator
        paginator = response.context_data['paginator']
        self.assertIsInstance(paginator, Paginator)

        cards_list = []
        for page_num in paginator.page_range:
            page_response = paginator.get_page(page_num)
            card = page_response.object_list

            cards_list.append(*card)

            # Check that the card matches the page. 'page_num-1' because index numbering starts from 0, pages from 1
            self.assertEquals(*card, self.cards[page_num-1])

        # Check object_list
        self.assertListEqual(cards_list, self.cards)


class CardsCreateTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='Test_1', password='123', email='test@test.test')
        self.collection = Collections.objects.create(owner=self.user, name='Test')
        self.url = reverse('cards:create_card')

    def test_get(self):
        self.client.force_login(self.user)

        response = self.client.get(self.url)

        self.assertTemplateUsed(response, 'cards/create_card.html')
        self.assertIsInstance(response.context['form'], CardForm)


    def test_post_valid(self):
        self.client.force_login(self.user)

        response = self.client.post(self.url, data={'english_word': 'aaa',
                                                    'russian_word': 'aaa',
                                                    'collection': self.collection})
        self.assertTemplateUsed(response, 'cards/create_card.html')
        form = response.context['form']
        print(response.context['form'])
        print(Cards.objects.first())
