import pytest
from quiz_exercise import display_question, get_user_choice

def test_display_question(capsys):
    question = {
        'Question': 'How much is 2+2?',
        'Options': ['1', '3', '4', '5'],
        'Answer': '4',
    }
    display_question(question)
    captured = capsys.readouterr()
    assert 'How much is 2+2?' in captured.out

def test_get_user_choice_valid_input(monkeypatch):
    user_input = '2\n'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    choice = get_user_choice(4)
    assert choice == 2

def test_get_user_choice_invalid_input_then_valid(monkeypatch):
    user_input = ['invalid', '2\n']
    monkeypatch.setattr('builtins.input', lambda _: user_input.pop(0))
    choice = get_user_choice(4)
    assert choice == 2

# Add more tests as needed

if __name__ == "__main__":
    pytest.main()
