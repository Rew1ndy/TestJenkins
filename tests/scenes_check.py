def test_scenes_exist():
    expected_scenes = {"bg2", "bg4", "bg5", "bg6", "black", "bg3"}
    found_scenes = set()
    
    with open("game/script.rpy", "r", encoding="utf-8") as f:
        for line in f:
            if line.strip().startswith("scene "):
                scene = line.split()[1].split(".")[0]  # Видаляємо розширення (напр., bg2.jpg → bg2)
                found_scenes.add(scene)
    
    missing = expected_scenes - found_scenes
    assert not missing, f"Відсутні сцени: {missing}"
