import pygame

pygame.init()


class Inputbox:
    """Класс окна для ввода текста"""
    def __init__(self, x_pos=200, y_pos=200, width=200, height=60, text='', text_color=(255, 255, 255),
                 active_color=(55, 55, 55), inactive_color=(32, 249, 7)):
        self.text = text
        self.font = pygame.font.SysFont('Georgia', 43, bold=True)
        self.input_box = pygame.Rect(x_pos, y_pos, width, height)
        self.text_color = text_color
        self.input_box_color = active_color
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.txt_surface = self.font.render(text, True, self.text_color)
        self.active = False

    def handle_event(self, event, new_score):
        """Распознавание введённого текста"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            if self.active:
                self.input_box_color = self.inactive_color
            else:
                self.input_box_color = self.active_color
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self.save_score(self.text, new_score)
                    self.text = ''
                    return True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, self.text_color)

    def update(self):
        """Обновление окна ввода текста чтобы соответствовать введённому тексту"""
        width = max(200, self.txt_surface.get_width() + 10)
        self.input_box.width = width

    def draw(self, screen):
        """Отрисовка окна ввода текста"""
        screen.blit(self.txt_surface, (self.input_box.x + 10, self.input_box.y + 3))
        pygame.draw.rect(screen, self.input_box_color, self.input_box, 2)

    def save_score(self, name, score):
        """Сохранение имени в рекорды"""
        input_file = open('scores.txt', 'r')
        scores = input_file.readlines()
        input_file.close()

        was_text_in_scores = False
        for (line_index, line) in enumerate(scores):
            divider_index = line.find("#")
            current_name = line[:divider_index]
            current_score = int(line[divider_index + 1:])

            if current_name == name:  # Если введённое имя уже присутствует в списках рекордов
                was_text_in_scores = True
                if score > current_score:
                    append = '\n'
                    if line_index == len(scores) - 1:
                        append = ''
                    scores[line_index] = line[:divider_index + 1] + str(score) + append

        if not was_text_in_scores:  # Если введённого имени в списках рекордов ещё нет
            scores.append(str(name + '#' + str(score) + '\n'))

        def sort_by_score(string):
            return int(string[string.find("#") + 1:])

        scores.sort(key=sort_by_score)  # Ключом является количество очков в каждой строке
        scores.reverse()

        output_file = open('scores.txt', 'w')
        output_file.truncate()
        for line in scores:
            output_file.write(line)
        return

