import pygame
import sys
class King:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(None, 25)  # Set font for text label

    def draw(self, screen):
        # Draw a red circle for the King piece
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 25)

        # Add text label for King piece
        label = self.font.render("K", True, (255, 255, 255))
        text_rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, text_rect)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Advisor:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(None, 25)  # Set font for text label

    def draw(self, screen):
        if self.color == "RED":
            piece_color = (255, 0, 0)
        else:
            piece_color = (0, 0, 0)

        # Draw a circle for the Advisor piece
        pygame.draw.circle(screen, piece_color, (self.x, self.y), 25)

        # Add text label for Advisor piece
        label = self.font.render("A", True, (255, 255, 255))
        text_rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, text_rect)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Elephant:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(None, 25)  # Set font for text label

    def draw(self, screen):
        if self.color == "RED":
            piece_color = (255, 0, 0)
        else:
            piece_color = (0, 0, 0)

        # Draw a circle for the Elephant piece
        pygame.draw.circle(screen, piece_color, (self.x, self.y), 25)

        # Add text label for Elephant piece
        label = self.font.render("E", True, (255, 255, 255))
        text_rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, text_rect)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class Horse:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(None, 25)  # Set font for text label

    def draw(self, screen):
        if self.color == "RED":
            piece_color = (255, 0, 0)
        else:
            piece_color = (0, 0, 0)

        # Draw a circle for the Horse piece
        pygame.draw.circle(screen, piece_color, (self.x, self.y), 25)

        # Add text label for Horse piece
        label = self.font.render("H", True, (255, 255, 255))
        text_rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, text_rect)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

class Chariot:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(None, 25)  # Set font for text label

    def draw(self, screen):
        if self.color == "RED":
            piece_color = (255, 0, 0)
        else:
            piece_color = (0, 0, 0)

        # Draw a circle for the Chariot piece
        pygame.draw.circle(screen, piece_color, (self.x, self.y), 25)

        # Add text label for Chariot piece
        label = self.font.render("C", True, (255, 255, 255))
        text_rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, text_rect)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Cannon:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(None, 25)  # Set font for text label

    def draw(self, screen):
        if self.color == "RED":
            piece_color = (255, 0, 0)
        else:
            piece_color = (0, 0, 0)

        # Draw a circle for the Cannon piece
        pygame.draw.circle(screen, piece_color, (self.x, self.y), 25)

        # Add text label for Cannon piece
        label = self.font.render("P", True, (255, 255, 255))
        text_rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, text_rect)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y


class Soldier:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.font = pygame.font.SysFont(None, 25)  # Set font for text label

    def draw(self, screen):
        if self.color == "RED":
            piece_color = (255, 0, 0)
        else:
            piece_color = (0, 0, 0)

        # Draw a circle for the Soldier piece
        pygame.draw.circle(screen, piece_color, (self.x, self.y), 25)

        # Add text label for Soldier piece
        label = self.font.render("S", True, (255, 255, 255))
        text_rect = label.get_rect(center=(self.x, self.y))
        screen.blit(label, text_rect)

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y