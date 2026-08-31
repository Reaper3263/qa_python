import pytest

from main import BooksCollector


@pytest.fixture(autouse=True)
def test_class_init(request):
    request.cls.collector = BooksCollector()
