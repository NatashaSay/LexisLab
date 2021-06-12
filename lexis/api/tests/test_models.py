import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

class TestWord:
    def test_model(self):
        obj = mixer.blend('api.Words')
        assert obj.pk == 1, 'Should create a Word instance'

    def test_translate(self):
        obj = mixer.blend('api.Words', content='Привіт')
        result = obj.translate()
        assert result == 'Hallo', 'Should translate a word'

    def test_translate_statement(self):
        obj = mixer.blend('api.Words', content='Привіт усім!')
        result = obj.translate()
        assert result == 'Hallo an alle!', 'Should translate a word'

    def test_translate_uk(self):
        obj = mixer.blend('api.Words', content='Hallo')
        result = obj.translate()
        assert result == 'Привіт', 'Should translate a word'

    def test_translate_uk_statement(self):
        obj = mixer.blend('api.Words', content='Hallo an alle!!')
        result = obj.translate()
        assert result == 'Привіт усім!', 'Should translate a word'


class ThemeTest:
    def test_model(self):
        obj = mixer.blend('api.Themes')
        assert obj.pk == 1, 'Should create a Theme instance'

    def test_translate(self):
        obj = mixer.blend('api.Themes', content='Навчання')
        result = obj.translate()
        assert result == 'Studie', 'Should translate a theme'