# reference: https://github.com/baraltech/Menu-System-PyGame

import pygame, sys
from arcade_model import *
from button import Button
from checkers import checkers
from tic_tac_toe import tic_tac_toe
from player_stats import player_stats
from connect_four import connect_4

pygame.init()

pygame.display.set_caption("Menu")


# MODEL
def process_win(winner, gameName):

    if gameName == "Checkers":
        if winner == "Player 1":
            CHECKERS_WINS[0] += 1
        elif winner == "Player 2":
            CHECKERS_WINS[1] += 1
    elif gameName == "Connect 4":
        if winner == "Player 1":
            CONNECT_4_WINS[0] += 1
        elif winner == "Player 2":
            CONNECT_4_WINS[1] += 1
    elif gameName == "Tic-Tac-Toe":
        if winner == "Player 1":
            TIC_TAC_TOE_WINS[0] += 1
        elif winner == "Player 2":
            TIC_TAC_TOE_WINS[1] += 1

    display_winner(winner)


# VIEW
def display_winner(winner):
    while True:
        WINNER_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        WINNER = winner + " wins"
        pygame.display.set_caption(WINNER)
        WINNER_TEXT = pygame.font.Font("assets/font.ttf", 50).render(
            WINNER, True, "White"
        )
        WINNER_RECT = WINNER_TEXT.get_rect(center=(400, 400))
        SCREEN.blit(WINNER_TEXT, WINNER_RECT)
        WINNER_BACK = Button(
            pos=(400, 600),
            input="MAIN MENU",
            font=pygame.font.Font("assets/font.ttf", 25),
            base="White",
            hover="Green",
        )

        WINNER_BACK.changeColor(WINNER_MOUSE_POS)
        WINNER_BACK.update(SCREEN)

        # CONTROLLER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if WINNER_BACK.checkForInput(WINNER_MOUSE_POS):
                    main_menu()

        pygame.display.update()


# MODEL
def play_checkers():
    pygame.display.set_caption("Checkers")
    SCREEN.fill("black")
    process_win(checkers(800, 8, 12, 12), "Checkers")


def play_connect_4():
    pygame.display.set_caption("Connect 4")
    SCREEN.fill("black")
    process_win(connect_4(), "Connect 4")


def play_tic_tac_toe():
    pygame.display.set_caption("Tic-Tac-Toe")
    SCREEN.fill("black")
    process_win(tic_tac_toe(800, 3), "Tic-Tac-Toe")


def main_menu():
    while True:
        # VIEW
        SCREEN.blit(BG, (0, 0))

        MENU_TEXT = pygame.font.Font("assets/font.ttf", 60).render(
            "MAIN MENU", True, "Grey"
        )
        MENU_RECT = MENU_TEXT.get_rect(center=(400, 100))

        CHECKERS_BUTTON = Button(
            pos=(400, 250),
            input="CHECKERS",
            font=pygame.font.Font("assets/font.ttf", 40),
            base="White",
            hover="Green",
        )
        CONNECT_4_BUTTON = Button(
            pos=(400, 325),
            input="CONNECT 4",
            font=pygame.font.Font("assets/font.ttf", 40),
            base="White",
            hover="Green",
        )
        TIC_TAC_TOE_BUTTON = Button(
            pos=(400, 400),
            input="TIC-TAC-TOE",
            font=pygame.font.Font("assets/font.ttf", 40),
            base="White",
            hover="Green",
        )
        PLAYER_STATS_BUTTON = Button(
            pos=(400, 475),
            input="PLAYER STATS",
            font=pygame.font.Font("assets/font.ttf", 40),
            base="White",
            hover="Green",
        )
        QUIT_BUTTON = Button(
            pos=(400, 625),
            input="QUIT",
            font=pygame.font.Font("assets/font.ttf", 40),
            base="White",
            hover="Green",
        )

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        menu_buttons(
            CHECKERS_BUTTON,
            CONNECT_4_BUTTON,
            TIC_TAC_TOE_BUTTON,
            PLAYER_STATS_BUTTON,
            QUIT_BUTTON,
        )

        pygame.display.update()


# CONTROLLER
def menu_buttons(
    CHECKERS_BUTTON,
    CONNECT_4_BUTTON,
    TIC_TAC_TOE_BUTTON,
    PLAYER_STATS_BUTTON,
    QUIT_BUTTON,
):

    MENU_MOUSE_POS = pygame.mouse.get_pos()

    for button in [
        CHECKERS_BUTTON,
        CONNECT_4_BUTTON,
        TIC_TAC_TOE_BUTTON,
        PLAYER_STATS_BUTTON,
        QUIT_BUTTON,
    ]:
        button.changeColor(MENU_MOUSE_POS)
        button.update(SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if CHECKERS_BUTTON.checkForInput(MENU_MOUSE_POS):
                play_checkers()
            if CONNECT_4_BUTTON.checkForInput(MENU_MOUSE_POS):
                play_connect_4()
            if TIC_TAC_TOE_BUTTON.checkForInput(MENU_MOUSE_POS):
                play_tic_tac_toe()
            if PLAYER_STATS_BUTTON.checkForInput(MENU_MOUSE_POS):
                player_stats()
            if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                pygame.quit()
                sys.exit()


main_menu()
