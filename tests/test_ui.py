def test_menu_options():
    required_options = [
        "Піти до бібліотеки",
        "Повернутись додому"
    ]
    
    with open("game/script.rpy", "r") as f:
        content = f.read()
        for option in required_options:
            assert option in content, f"Опція '{option}' відсутня в меню"