from abc import ABC, abstractmethod
import unittest
from unittest.mock import Mock

class HelpRequest:
    def __init__(self, description):
        self.description = description

class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass

class Assistant(Handler):
    def handle(self, request):
        if "простой вопрос" in request.description:
            return "Assistant решает вопрос."
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return "Запрос не может быть обработан."

class Professor(Handler):
    def handle(self, request):
        if request.description.strip() == "сложный вопрос" or request.description.strip().startswith("сложный вопрос "):
            return "Professor решает вопрос."
        elif self._next_handler:
            return self._next_handler.handle(request)
        else:
            return "Запрос не может быть обработан."

class Dean(Handler):
    def handle(self, request):
        return "Dean решает вопрос."

def demo():
    assistant = Assistant()
    professor = Professor()
    dean = Dean()

    assistant.set_next(professor).set_next(dean)

    requests = [
        HelpRequest("простой вопрос про расписание"),
        HelpRequest("сложный вопрос"),
        HelpRequest("очень сложный вопрос по политике факультета")
    ]

    for r in requests:
        print(assistant.handle(r))

class TestChainWithMock(unittest.TestCase):
    def test_handle_calls_next_when_not_handled(self):
        assistant = Assistant()
        mock_handler = Mock()
        mock_handler.handle.return_value = "Mocked handler processed"
        assistant.set_next(mock_handler)

        req = HelpRequest("сложный вопрос")

        response = assistant.handle(req)

        mock_handler.handle.assert_called_once_with(req)
        self.assertEqual(response, "Mocked handler processed")

    def test_assistant_handles_easy_question(self):
        assistant = Assistant()
        req = HelpRequest("простой вопрос")
        self.assertEqual(assistant.handle(req), "Assistant решает вопрос.")

if __name__ == "__main__":
    demo()
    print("\nЗапуск тестов...\n")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
