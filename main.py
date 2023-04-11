import sys

sys.path.append('../Project_1_github_version/game')
sys.path.append('../Project_1_github_version/menu')

from game import Game
from main_menu import MainMenu
from pause_menu import PauseMenu
from enter_your_name_menu import EnterYourNameMenu
from records_menu import RecordsMenu

game_process = Game()
main_menu_process = MainMenu()
pause_menu_process = PauseMenu(game_process.game_screen)
enter_your_name_menu_process = EnterYourNameMenu(game_process.game_screen)
records_menu_process = RecordsMenu()

while True:
    """Главный цикл программы. Обеспечивает взаимодействие главного меню, меню паузы и игры"""
    if main_menu_process.main_menu.run:
        main_menu_process.run_main_menu()
    if main_menu_process.main_menu.go_to_endless_mode:
        main_menu_process.main_menu.go_to_endless_mode = False
        main_menu_process.main_menu.run = False
        game_process.game.run = True
    if main_menu_process.main_menu.go_to_records_menu:
        main_menu_process.main_menu.go_to_records_menu = False
        main_menu_process.main_menu.run = False
        records_menu_process.records_menu.run = True

    if game_process.game.run:
        game_process.run_game()
    if game_process.game.paused:
        pause_menu_process.pause_menu.run = True
    if game_process.game.entering_name:
        enter_your_name_menu_process.enter_your_name_menu.run = True

    if pause_menu_process.pause_menu.run:
        pause_menu_process.run_pause_menu()
    if pause_menu_process.pause_menu.resume:
        pause_menu_process.pause_menu.resume = False
        pause_menu_process.pause_menu.run = False
        game_process.game.paused = False
    if pause_menu_process.pause_menu.restart:
        pause_menu_process.pause_menu.restart = False
        pause_menu_process.pause_menu.run = False
        game_process.game.paused = False
        game_process.game.reset()
    if pause_menu_process.pause_menu.go_to_main_menu:
        pause_menu_process.pause_menu.go_to_main_menu = False
        pause_menu_process.pause_menu.run = False
        game_process.game.paused = False
        game_process.game.run = False
        main_menu_process.main_menu.run = True

    if enter_your_name_menu_process.enter_your_name_menu.run:
        enter_your_name_menu_process.run_enter_your_name_menu(game_process.game.prev_score)
    if enter_your_name_menu_process.enter_your_name_menu.restart:
        enter_your_name_menu_process.enter_your_name_menu.restart = False
        enter_your_name_menu_process.enter_your_name_menu.run = False
        game_process.game.entering_name = False
        game_process.game.reset()
    if enter_your_name_menu_process.enter_your_name_menu.go_to_main_menu:
        enter_your_name_menu_process.enter_your_name_menu.go_to_main_menu = False
        enter_your_name_menu_process.enter_your_name_menu.run = False
        game_process.game.entering_name = False
        game_process.game.run = False
        main_menu_process.main_menu.run = True

    if records_menu_process.records_menu.run:
        records_menu_process.run_records_menu()
    if records_menu_process.records_menu.exit:
        records_menu_process.records_menu.exit = False
        records_menu_process.records_menu.run = False
        main_menu_process.main_menu.run = True
