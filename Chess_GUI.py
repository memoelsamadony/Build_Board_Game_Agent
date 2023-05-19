import Chess_Class
import pygame as py
import os
import Computer_Class
from multiprocessing import Process, Queue
import sys
import pygame_menu as py_menu

"""Variables"""
WIDTH = HEIGHT = 512  # width and height of the chess board
DIMENSION = 8  # the dimensions of the chess board
SQ_SIZE = HEIGHT // DIMENSION  # the size of each of the squares in the board
MAX_FPS = 25  # FPS for animations
IMAGES = {}  # images for the chess pieces


# TODO: AI black has been worked on. Mirror progress for other two modes
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
    Animating a move with gentle movement and dark blue highlighting
    """
    start_square = py.Rect(move.start_col * SQ_SIZE, move.start_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
    end_square = py.Rect(move.end_col * SQ_SIZE, move.end_row * SQ_SIZE, SQ_SIZE, SQ_SIZE)
    d_row = move.end_row - move.start_row
    d_col = move.end_col - move.start_col
    frames_per_square = 5  # frames to move one square
    frame_count = (abs(d_row) + abs(d_col)) * frames_per_square

    # highlight start square in dark blue
    py.draw.rect(screen, py.Color('dark blue'), start_square)
    draw_board(screen)
    draw_Pieces(screen, board)
    py.display.flip()

    for frame in range(frame_count + 1):
        # calculate the current position of the moving piece
        row = move.start_row + d_row * frame / frame_count
        col = move.start_col + d_col * frame / frame_count

        # draw the board and the moving piece at its current position
        draw_board(screen)
        py.draw.rect(screen, py.Color('dark blue'), end_square)
        screen.blit(IMAGES[move.piece_moved], py.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))
        draw_Pieces(screen, board)
        py.display.flip()
        clock.tick(30)

    # highlight end square in dark blue
    py.draw.rect(screen, py.Color('dark blue'), end_square)
    draw_board(screen)
    draw_Pieces(screen, board)
    py.display.flip()

    # highlight end square in dark blue
    py.draw.rect(screen, py.Color('dark blue'), end_square)
    draw_Pieces(screen, board)
    py.display.flip()




def display_menu(screen,params):
    
    
    # create menu for the user to choose which aalgorithm is selected
    # from 'Alpha-beta' and 'minimax' also to choose whether 
    # iterative deepening is used or not 
    # and to choose the difficulty of the game
    # and to choose the color of the player
    def set_algorithm(x,index):
        params[0] = x[0][1]

    def set_search_tool(x,index):
        params[1] = x[0][1]

    def set_difficulty(x,index):
        params[2] = x[0][1]

    def set_color(x,index):
        params[3] = x[0][1]

    def start_game():
        menu.disable()
        
    

    menu = py_menu.Menu('Welcome to Chess',512, 512,theme=py_menu.themes.THEME_DARK)
    menu.add.selector('Algorithm :', [('Alpha-Beta', 'Alpha-Beta'), ('Minimax', 'Minimax')], onchange=set_algorithm)
    menu.add.selector('Search Tool :', [('Iterative Deepening', True), ('Depth Limited', False)], onchange=set_search_tool)
    menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=set_difficulty)
    menu.add.selector('Color :', [('White', 'White'), ('Black', 'Black')], onchange=set_color)
    menu.add.button('Play', start_game)
    menu.add.button('Quit', py_menu.events.EXIT)



    menu.mainloop(screen)
    
        
        
def main():
    """
    The main driver for our code.
    This will handle user input and updating the graphics.
    """
    params = [None,None,None,None]
    py.init()
    screen = py.display.set_mode((WIDTH , HEIGHT))
    py.display.set_caption('Chess')
    display_menu(screen,params)
    clock = py.time.Clock()
    screen.fill(py.Color("white"))
    game_state = Chess_Class.GameState()
    valid_moves = game_state.getValidMoves()
    move_made = False  # flag variable for when a move is made
    animate = False  # flag variable for when we should animate a move
    load_images()  # do this only once before while loop
    running = True
    game_over = False
    ai_thinking = False
    move_finder_process = None
    
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
            player_two = Computer_Class.AlphaBetaAgent(1)
        else:
            player_one = Computer_Class.AlphaBetaAgent(1)
            player_two = Computer_Class.MinimaxAgent(params[2])

    while running:
        for e in py.event.get():
            if e.type == py.QUIT:
                py.quit()
                sys.exit()
            
        current = player_one if game_state.white_to_move else player_two
        # AI move finder
        if not game_over :
            if not ai_thinking:
                ai_thinking = True
                return_queue = Queue()  # used to pass data between threads
                move_finder_process = Process(target=current.findBestMove, args=(game_state, valid_moves, return_queue, params[1]))
                move_finder_process.start()

            if not move_finder_process.is_alive():
                ai_move = return_queue.get()
                if ai_move is None:
                    ai_move = current.findRandomMove(valid_moves)
                game_state.makeMove(ai_move)
                move_made = True
                animate = True
                ai_thinking = False

        if move_made:
            if animate:
                animateMove(game_state.move_log[-1], screen, game_state.board, clock)
            valid_moves = game_state.getValidMoves()
            move_made = False
            animate = False
            

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

        clock.tick(MAX_FPS)
        py.display.flip()



def draw_text(screen, text):
    font = py.font.SysFont("Helvitca", 32, True, False)
    text_object = font.render(text, False, py.Color("Black"))
    text_location = py.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2,
                                                      HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)



if __name__ == "__main__":
    main()