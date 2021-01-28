from django.test import TestCase
from .utility import *
# Create your tests here.
class TestContentAPI(TestCase):
    def test_get_homepage_article(self):
        homepage_article = get_homepage_article()
        homepage_article_uuid = "a7acd8c8-c5ce-11e7-9fa6-0050569d4be0"
        self.assertEqual(homepage_article.get("uuid"),homepage_article_uuid)


    def test_get_article_by_uuid(self):
        homepage_article_uuid = "a7acd8c8-c5ce-11e7-9fa6-0050569d4be0"
        homepage_article = get_article_by_uuid(homepage_article_uuid)
        homepage_promo = 'As autumn marches on, the trees are losing their leaves, and Barrick is losing its glitter.'
        self.assertEqual(homepage_article.get("promo"),homepage_promo)


        test_article_1_uuid = 'f1a541a2-c45e-11e7-9008-0050569d4be0'
        test_article_1 = get_article_by_uuid(test_article_1_uuid)
        test_article_1_promo = "This Fool digs deep into Intel's latest quarterly filing. "
        self.assertEqual(test_article_1.get("promo"),test_article_1_promo)

        test_article_2_uuid = '9059ec08-c5f4-11e7-bec4-0050569d32b9'
        test_article_2 = get_article_by_uuid(test_article_2_uuid)
        test_article_2_promo = "Some revenue timing issues and unfavorable foreign currency changes make the transmission utility's results look worse than they are. "
        self.assertEqual(test_article_2.get("promo"),test_article_2_promo)


    def test_get_random_articles(self):
        count  = 3
        homepage_article_uuid = "a7acd8c8-c5ce-11e7-9fa6-0050569d4be0"
        random_articles = get_random_articles(count)
        self.assertEqual(len(random_articles),count)
        # test for all unique and does not contain homepage articles
        uuid_set = {}
        uuids_are_unique = True
        for article in random_articles:
            article_uuid = article.get("uuid")
            if article_uuid in uuid_set:
                unique_uuids = False
        self.assertEqual(uuids_are_unique,True)

        self.assertEqual( homepage_article_uuid in random_articles,False)