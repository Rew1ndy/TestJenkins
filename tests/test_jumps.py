import re

def test_jumps():
    labels = []
    jumps = []
    
    # Парсинг файлів .rpy
    with open("game/script.rpy", "r") as f:
        content = f.read()
        labels.extend(re.findall(r"label (\w+):", content))
        jumps.extend(re.findall(r"jump (\w+)", content))
    
    # Перевірка валідності переходів
    for jump in jumps:
        assert jump in labels, f"Label '{jump}' не існує (jump {jump})"