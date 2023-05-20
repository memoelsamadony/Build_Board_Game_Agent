import os
import sys
import time
from multiprocessing import Process, Queue

import Chess_Class
import Computer_Class
import pygame as py
import pygame_menu as py_menu
from PIL import ImageColor

golden= ImageColor.getrgb(color='goldenrod')
"""Variables"""
WIDTH = HEIGHT = 512  # width and height of the chess board
DIMENSION = 8  # the dimensions of the chess board
SQ_SIZE = HEIGHT // DIMENSION  # the size of each of the squares in the board
MAX_FPS = 25  # FPS for animations
IMAGES = {}  # images for the chess pieces
MENU_SIZE = (640, 480)
# TODO: AI black has been worked on. Mirror progress for other two modes

py.mixer.init()
py.mixer.music.load("Chess_Music.mp3")
py.mixer.music.play(-1) 

def load_images():
    '''
    Load images for the chess pieces
    '''
    pieces = pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for p in pieces:
        IMAGES[p] = py.transform.scale(py.image.load("images/" + p + ".png"), (SQ_SIZE, SQ_SIZE-15))


def draw_game_state(screen, game_state):
    ''' Draw the complete chess board with pieces
    Keyword arguments:
        :param screen       -- the pygame screen
        :param game_state   -- the state of the current chess game
    '''
    
    draw_board(screen)
    draw_Pieces(screen, game_state.board)


def draw_board(screen):
    ''' Draw the board image
    :param screen:          -- the pygame screen
    '''
    board_image = py.image.load(os.path.join('images', 'board.png'))
    board_image = py.transform.scale(board_image, (WIDTH, HEIGHT))
    screen.blit(board_image, (0, 0))

def draw_Pieces(screen, board):
    """
    Draw the pieces on the board using the current game_state.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                # get the scaled image size
                img_size = IMAGES[piece].get_size()
                # calculate the new x and y coordinates
                x_coord = column * SQ_SIZE + (SQ_SIZE - img_size[0]) / 2
                y_coord = row * SQ_SIZE + (SQ_SIZE - img_size[1]) / 2
                # draw the piece at the new location
                screen.blit(IMAGES[piece], py.Rect(x_coord, y_coord, img_size[0],img_size[1]))
                                                   
def animateMove(move, screen, board, clock):
    """
    Animating a move with gentle movement and golden highlighting
    """
    start_square = py.Rect(move.start_col * SQ_SIZE, move.start_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
    end_square = py.Rect(move.end_col * SQ_SIZE, move.end_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
    d_row = move.end_row - move.start_row
    d_col = move.end_col - move.start_col
    frames_per_square = 5  # frames to move one square
    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square

    # highlight start square in golden
    py.draw.rect(screen, py.Color(golden), start_square)
    draw_board(screen)
    draw_Pieces(screen, board)
    py.display.flip()

    for frame in range(frame_count + 1):
        # calculate the current position of the moving piece
        row = move.start_row + d_row * frame / frame_count
        col = move.start_col + d_col * frame / frame_count

        # draw the board and the moving piece at its current position
        draw_board(screen)
        py.draw.rect(screen, py.Color(golden), end_square)
        screen.blit(IMAGES[move.piece_moved], py.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        draw_Pieces(screen, board)
        py.display.flip()
        clock.tick(30)

    # highlight end square in golden
    py.draw.rect(screen, py.Color(golden), end_square)
    draw_board(screen)
    draw_Pieces(screen, board)
    py.display.flip()

    # highlight end square in golden
    py.draw.rect(screen, py.Color(golden), end_square)
    draw_Pieces(screen, board)
    py.display.flip()


# background_image = py_menu.BaseImage(image_path="images/background.png")
# def main_background() -> None:
#     # Background color of the main menu, on this function user can plot images, play sounds, etc.
#     background_image.draw(screen)

def display_menu(screen,params):

    
    clock = py.time.Clock()
    main_menu_theme = py_menu.themes.THEME_DARK.copy()
    main_menu_theme.background_color = py_menu.BaseImage(
        image_path="images/background.png"
    )
    

    main_menu = py_menu.Menu(
        height=MENU_SIZE[1] ,
        #  # User press ESC button
        theme=main_menu_theme,
        title='Welcome to Chess Game!',
        width=MENU_SIZE[0] 
    )

    theme_bg_image = py_menu.themes.THEME_DARK.copy()
    theme_bg_image.background_color = py_menu.BaseImage(
        image_path="images/Background2.jpg"
    )
    theme_bg_image.title_font_size = 40
    menu_Algorithm = py_menu.Menu(
        height=MENU_SIZE[1],
        onclose=py_menu.events.EXIT,
        theme=theme_bg_image,
        title='Choose an Algorithm',
        width=MENU_SIZE[0] ,

)
    def set_algorithm(x,index):
        params[0] = x 
    menu_Algorithm.add.selector('Algorithm :', [('Alpha-Beta', 'Alpha_beta'), ('Minimax', 'Minimax')], onchange=set_algorithm)

    menu_Tool = py_menu.Menu(
        height=MENU_SIZE[1] ,
        onclose=py_menu.events.EXIT,
        theme=theme_bg_image,
        title='Choose search tool',
        width=MENU_SIZE[0] ,
    )
   
    def set_search_tool(x,index):
        params[1] = x
    menu_Tool.add.selector('Search Tool :', [('Iterative Deepening', True), ('Depth Limited', False)], onchange=set_search_tool)

    menu_Difficulty = py_menu.Menu(
        height=MENU_SIZE[1] ,
        onclose=py_menu.events.EXIT,
        theme=theme_bg_image,
        title='Choose difficulty',
        width=MENU_SIZE[0] ,
    )
    def set_difficulty(x,index):
        params[2] = x[0][1]
    menu_Difficulty.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)

    menu_Color = py_menu.Menu(
        height=MENU_SIZE[1] ,
        onclose=py_menu.events.EXIT,
        theme=theme_bg_image,
        title='Choose color',
        width=MENU_SIZE[0] ,
    )
    def set_color(x,index):
        params[3] = x 
    menu_Color.add.selector('Color :', [('White', 'White'), ('Black', 'Black')], onchange=set_color)
    def start_game():
        main_menu.disable()
    main_menu.add.button('Algorithm', menu_Algorithm)
    main_menu.add.button('Search Tool', menu_Tool)
    main_menu.add.button('Difficulty',menu_Difficulty)
    main_menu.add.button('Color',menu_Color)
    main_menu.add.button('play',start_game)
    main_menu.add.button('Quit', py_menu.events.EXIT)
    
    # Tick
    clock.tick(MAX_FPS)

        # Main menu
    
    main_menu.mainloop(screen, fps_limit=MAX_FPS)

        # Flip surface
    py.display.flip()

    
        
        
def main():
    """
    The main driver for our code.
    This will handle user input and updating the graphics.
    """
    params = ['Minimax',True,2,'White']
    py.init()
    screen = py.display.set_mode(MENU_SIZE, py.RESIZABLE)
    py.display.set_caption('Chess Game')
    display_menu(screen,params)
    clock = py.time.Clock()
    screen.fill(py.Color("white"))
    game_state = Chess_Class.GameState()
    valid_moves = game_state.getValidMoves()
    move_made = False  # flag variable for when a move is made
    load_images()  # do this only once before while loop
    screen = py.display.set_mode((WIDTH, HEIGHT), py.RESIZABLE)
    running = True
    game_over = False
    agent_working = False
    move_finder_process = None
    player_one_time = []
    player_two_time = []
    player_one_nodes = []
    player_two_nodes = []
    
    # make the if conditions based on the params
    if params[0] == 'Alpha-Beta':
        if params[3] == 'White':
            player_one = Computer_Class.AlphaBetaAgent(params[2])
            player_two = Computer_Class.AlphaBetaAgent(1)
        else:
            player_one = Computer_Class.AlphaBetaAgent(1)
            player_two = Computer_Class.AlphaBetaAgent(params[2])
    else:
        if params[3] == 'White':
            player_one = Computer_Class.MinimaxAgent(params[2])
            player_two = Computer_Class.AlphaBetaAgent(2)
        else:
            player_one = Computer_Class.AlphaBetaAgent(2)
            player_two = Computer_Class.MinimaxAgent(params[2])

    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                py.quit()
                sys.exit()
            
        current = player_one if game_state.white_to_move else player_two
        # AI move finder
        if not game_over :
            if not agent_working:
                return_queue = Queue()  # used to pass data between threads
                nodes_que = Queue()
                move_finder_process = Process(target=current.findBestMove, args=(game_state, valid_moves, return_queue,nodes_que, params[1]))
                move_finder_process.start()
                start_time = time.time()
                agent_working = True

            if not move_finder_process.is_alive():
                ai_move = return_queue.get()
                if ai_move is None:
                    ai_move = current.findRandomMove(valid_moves)
                game_state.makeMove(ai_move)
                end_time = time.time()
                time_taken = end_time - start_time
                if game_state.white_to_move:
                    player_one_time.append(time_taken)
                    player_one_nodes.append(nodes_que.get())
                else:
                    player_two_time.append(time_taken)
                    player_two_nodes.append(nodes_que.get())
                move_made = True
                agent_working = False

        if move_made:
            animateMove(game_state.move_log[-1], screen, game_state.board, clock)
            valid_moves = game_state.getValidMoves()
            move_made = False
            

        draw_game_state(screen, game_state)

        

        if game_state.checkmate:
            game_over = True
            if game_state.white_to_move:
                draw_text(screen, "Black wins by checkmate")
            else:
                draw_text(screen, "White wins by checkmate")

        elif game_state.stalemate:
            game_over = True
            draw_text(screen, "Stalemate")
        
        if game_over:
            with open("data.txt", "w") as f:
                f.write(str(player_one_time) + "\n")
                f.write(str(player_two_time) + "\n")
                f.write(str(player_one_nodes) + "\n")
                f.write(str(player_two_nodes) + "\n")
                f.close()

        clock.tick(MAX_FPS)
        py.display.flip()
    py.mixer.music.stop()
    py.quit()
    sys.exit()




def draw_text(screen, text):
    font = py.font.SysFont("Helvitca", 32, True, False)
    text_object = font.render(text, False, py.Color("Black"))
    text_location = py.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2,
                                                      HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)



if __name__ == "__main__":
    main()