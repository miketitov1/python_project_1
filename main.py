from game.game import Game
from menu.main_menu import MainMenu
from menu.pause_menu import PauseMenu
from menu.enter_your_name_menu import EnterYourNameMenu
from menu.records_menu import RecordsMenu


game_process = Game()
main_menu_process = MainMenu()
pause_menu_process = PauseMenu(game_process.game_screen)
enter_your_name_menu_process = EnterYourNameMenu(game_process.game_screen)
records_menu_process = RecordsMenu()

def main_process():
    while True:
        """Главный цикл программы. Обеспечивает взаимодействие главного меню, меню паузы и игры"""
        if main_menu_process.main_menu.run:  # Главное меню
            main_menu_process.run_main_menu()
        if main_menu_process.main_menu.go_to_endless_mode:  # Переход из главного меню в игру
            main_menu_process.main_menu.go_to_endless_mode = False
            main_menu_process.main_menu.run = False
            game_process.game.run = True
        if main_menu_process.main_menu.go_to_records_menu:  # Переход из главного меню в меню рекордов
            main_menu_process.main_menu.go_to_records_menu = False
            main_menu_process.main_menu.run = False
            records_menu_process.records_menu.run = True

        if game_process.game.run:  # Игра
            game_process.run_game()
        if game_process.game.paused:  # Переход из игры в меню паузы
            pause_menu_process.pause_menu.run = True
        if game_process.game.entering_name:  # Переход из игры в меню выбора имени (при проигрыше)
            enter_your_name_menu_process.enter_your_name_menu.run = True

        if pause_menu_process.pause_menu.run:  # Меню паузы
            pause_menu_process.run_pause_menu()
        if pause_menu_process.pause_menu.resume:  # Переход из меню паузы в игру
            pause_menu_process.pause_menu.resume = False
            pause_menu_process.pause_menu.run = False
            game_process.game.paused = False
        if pause_menu_process.pause_menu.restart:  # Рестарт игры из меню паузы
            pause_menu_process.pause_menu.restart = False
            pause_menu_process.pause_menu.run = False
            game_process.game.paused = False
            game_process.game.reset()
        if pause_menu_process.pause_menu.go_to_main_menu:  # Переход в главное меню из меню паузы
            pause_menu_process.pause_menu.go_to_main_menu = False
            pause_menu_process.pause_menu.run = False
            game_process.game.paused = False
            game_process.game.run = False
            main_menu_process.main_menu.run = True

        if enter_your_name_menu_process.enter_your_name_menu.run:  # Меню выбора имени
            enter_your_name_menu_process.run_enter_your_name_menu(game_process.game.prev_score)
        if enter_your_name_menu_process.enter_your_name_menu.restart:  # Рестарт игры из меню выбора имени
            enter_your_name_menu_process.enter_your_name_menu.restart = False
            enter_your_name_menu_process.enter_your_name_menu.run = False
            game_process.game.entering_name = False
            game_process.game.reset()
        if enter_your_name_menu_process.enter_your_name_menu.go_to_main_menu:  # Переход в главное меню из меню выбора имени
            enter_your_name_menu_process.enter_your_name_menu.go_to_main_menu = False
            enter_your_name_menu_process.enter_your_name_menu.run = False
            game_process.game.entering_name = False
            game_process.game.run = False
            main_menu_process.main_menu.run = True

        if records_menu_process.records_menu.run:  # Меню рекордов
            records_menu_process.run_records_menu()
        if records_menu_process.records_menu.exit:  # Переход из меню рекордов в главное меню
            records_menu_process.records_menu.exit = False
            records_menu_process.records_menu.run = False
            main_menu_process.main_menu.run = True


main_process()
