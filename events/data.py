from copy import deepcopy
from typing import Any

_EVENTS: list[dict[str, Any]] = [
    {
        "id": 1,
        "title": "Python Data Science Conf",
        "description": "Ежегодная конференция по машинному обучению и анализу данных.",
        "category": "Technology",
        "location": "Москва, ул. Тверская, 12",
        "status": "upcoming",
    },
    {
        "id": 2,
        "title": "Городской полумарафон «Осенний старт»",
        "description": "Забег на дистанции 5, 10 и 21 км для всех желающих.",
        "category": "Sport",
        "location": "Парк Горького, центральная набережная",
        "status": "open_for_registration",
    },
    {
        "id": 3,
        "title": "Мастер-класс по академическому рисунку",
        "description": "Практическое занятие по основам скетчинга и композиции.",
        "category": "Education",
        "location": "Арт-пространство «Смена», аудитория 3",
        "status": "ongoing",
    },
    {
        "id": 4,
        "title": "Джазовый вечер под открытым небом",
        "description": "Выступление джазового квартета с классическими стандартами.",
        "category": "Entertainment",
        "location": "Летний амфитеатр «Зеленый театр»",
        "status": "completed",
    },
    {
        "id": 5,
        "title": "Благотворительная ярмарка и своп",
        "description": "Обмен книгами и растениями, сбор средств в приюты для животных.",
        "category": "Other",
        "location": "Общественный центр «Маяк»",
        "status": "upcoming",
    },
    {
        "id": 6,
        "title": "AI & Robotics Summit",
        "description": "Выставка достижений в области робототехники и автономных систем.",
        "category": "Technology",
        "location": "Экспоцентр, павильон 4",
        "status": "planned",
    },
    {
        "id": 7,
        "title": "Открытый турнир по настольному теннису",
        "description": "Любительские одиночные и парные соревнования со свободным входом.",
        "category": "Sport",
        "location": "Спортивный комплекс «Арена»",
        "status": "cancelled",
    },
    {
        "id": 8,
        "title": "Курс лекций: Введение в критическое мышление",
        "description": "Серия открытых семинаров по когнитивным искажениям и логике.",
        "category": "Education",
        "location": "Онлайн (платформа Zoom)",
        "status": "ongoing",
    },
    {
        "id": 9,
        "title": "Фестиваль независимого кино «Кадр»",
        "description": "Показ короткометражных фильмов молодых режиссеров и дискуссии.",
        "category": "Entertainment",
        "location": "Кинотеатр «Иллюзион»",
        "status": "upcoming",
    },
    {
        "id": 10,
        "title": "Экологический субботник в сосновом бору",
        "description": "Уборка территории заказника и высадка саженцев.",
        "category": "Other",
        "location": "Городской лесопарк, центральный вход",
        "status": "completed",
    },
]

_next_id = 11


def list_events() -> list[dict[str, Any]]:
    return deepcopy(_EVENTS)


def get_event(event_id: int) -> dict[str, Any] | None:
    for event in _EVENTS:
        if event["id"] == event_id:
            return deepcopy(event)
    return None


def create_event(
    *,
    title: str,
    description: str,
    category: str,
    location: str,
    status: str = "upcoming",
) -> dict[str, Any]:
    global _next_id

    event = {
        "id": _next_id,
        "title": title,
        "description": description,
        "category": category,
        "location": location,
        "status": status,
    }

    _EVENTS.append(event)
    _next_id += 1

    return deepcopy(event)


def update_event(
    event_id: int,
    *,
    title: str,
    description: str,
    category: str,
    location: str,
    status: str,
) -> dict[str, Any] | None:
    for event in _EVENTS:
        if event["id"] == event_id:
            event["title"] = title
            event["description"] = description
            event["category"] = category
            event["location"] = location
            event["status"] = status
            return deepcopy(event)
    return None


def delete_event(event_id: int) -> bool:
    global _EVENTS

    initial_len = len(_EVENTS)
    _EVENTS = [event for event in _EVENTS if event["id"] != event_id]
    return len(_EVENTS) < initial_len