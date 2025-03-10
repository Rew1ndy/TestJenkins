def test_all_characters_have_lines():
    characters = {"e", "a"}
    found = set()
    
    with open("game/script.rpy", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith(tuple(characters)):
                char = line.split()[0]
                found.add(char)
    
    missing = characters - found
    assert not missing, f"Персонажі без реплік: {missing}"
