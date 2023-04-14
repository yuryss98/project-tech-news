import pytest
from unittest.mock import patch
from tech_news.analyzer.reading_plan import (
    ReadingPlanService,
)  # noqa: F401, E261, E501


@pytest.fixture
def mock_return_value():
    return {
        "readable": [
            {
                "unfilled_time": 3,
                "chosen_news": [
                    (
                        "Não deixe para depois",
                        4,
                    ),
                    (
                        "Selenium, BeautifulSoup ou Parsel?",
                        3,
                    ),
                ],
            },
            {
                "unfilled_time": 0,
                "chosen_news": [
                    (
                        "Pytest + Faker: a combinação poderosa dos testes!",
                        10,
                    )
                ],
            },
        ],
        "unreadable": [
            ("FastAPI e Flask: frameworks para APIs em Python", 15),
            ("A biblioteca Pandas e o sucesso da linguagem Python", 12),
        ],
    }


def mocked_data():
    return [
        {"title": "Não deixe para depois", "reading_time": 4},
        {"title": "Selenium, BeautifulSoup ou Parsel?", "reading_time": 3},
        {
            "title": "Pytest + Faker: a combinação poderosa dos testes!",
            "reading_time": 10,
        },
        {
            "title": "FastAPI e Flask: frameworks para APIs em Python",
            "reading_time": 15,
        },
        {
            "title": "A biblioteca Pandas e o sucesso da linguagem Python",
            "reading_time": 12,
        },
    ]


def test_reading_plan_group_news(mock_return_value):
    with patch(
        "tech_news.analyzer.reading_plan.ReadingPlanService._db_news_proxy",
        mocked_data,
    ):
        result = ReadingPlanService.group_news_for_available_time(10)

        assert result == mock_return_value

    with pytest.raises(
        ValueError, match="Valor 'available_time' deve ser maior que zero"
    ):
        FILE_BASE_PATH = "tech_news.analyzer.reading_plan"
        with patch(
            f"{FILE_BASE_PATH}.ReadingPlanService._db_news_proxy",
            mocked_data,
        ):
            ReadingPlanService.group_news_for_available_time(0)
