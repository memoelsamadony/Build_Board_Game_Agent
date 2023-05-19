"""
Handling the AI moves.
"""
import random
import copy

class BaseAgent:
    def __init__(self, max_depth=3):

        self.piece_score = {"K": 0, "Q": 9, "R": 5, "B": 3, "N": 3, "p": 1}

        self.knight_scores = [[0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0],
                        [0.1, 0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.1],
                        [0.2, 0.5, 0.6, 0.65, 0.65, 0.6, 0.5, 0.2],
                        [0.2, 0.55, 0.65, 0.7, 0.7, 0.65, 0.55, 0.2],
                        [0.2, 0.5, 0.65, 0.7, 0.7, 0.65, 0.5, 0.2],
                        [0.2, 0.55, 0.6, 0.65, 0.65, 0.6, 0.55, 0.2],
                        [0.1, 0.3, 0.5, 0.55, 0.55, 0.5, 0.3, 0.1],
                        [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]]

        self.bishop_scores = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                        [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.6, 0.6, 0.5, 0.4, 0.2],
                        [0.2, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.2],
                        [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                        [0.2, 0.6, 0.6, 0.6, 0.6, 0.6, 0.6, 0.2],
                        [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                        [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

        self.rook_scores = [[0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25],
                    [0.5, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.5],
                    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                    [0.0, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0],
                    [0.25, 0.25, 0.25, 0.5, 0.5, 0.25, 0.25, 0.25]]

        self.queen_scores = [[0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                        [0.2, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                        [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.4, 0.2],
                        [0.2, 0.4, 0.5, 0.4, 0.4, 0.4, 0.4, 0.2],
                        [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0]]

        self.pawn_scores = [[0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8],
                    [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                    [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3],
                    [0.25, 0.25, 0.3, 0.45, 0.45, 0.3, 0.25, 0.25],
                    [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
                    [0.25, 0.15, 0.1, 0.2, 0.2, 0.1, 0.15, 0.25],
                    [0.25, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.25],
                    [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]]

        self.piece_position_scores = {"wN": self.knight_scores,
                                "bN": self.knight_scores[::-1],
                                "wB": self.bishop_scores,
                                "bB": self.bishop_scores[::-1],
                                "wQ": self.queen_scores,
                                "bQ": self.queen_scores[::-1],
                                "wR": self.rook_scores,
                                "bR": self.rook_scores[::-1],
                                "wp": self.pawn_scores,
                                "bp": self.pawn_scores[::-1]}

        self.CHECKMATE = 1000
        self.STALEMATE = 0
        self.DEPTH = max_depth


    def findBestMove(self,game_state, valid_moves,que):
        pass


    def Search(self,game_state, valid_moves, depth, alpha, beta, turn_multiplier):
        pass


    def EvaluateBoard(self,game_state):
        """
        Score the board. A positive score is good for white, a negative score is good for black.
        """
        if game_state.checkmate:
            if game_state.white_to_move:
                return -self.CHECKMATE  # black wins
            else:
                return self.CHECKMATE  # white wins
        elif game_state.stalemate:
            return self.STALEMATE
        score = 0
        for row in range(len(game_state.board)):
            for col in range(len(game_state.board[row])):
                piece = game_state.board[row][col]
                if piece != "--":
                    piece_position_score = 0
                    if piece[1] != "K":
                        piece_position_score = self.piece_position_scores[piece][row][col]
                    if piece[0] == "w":
                        score += self.piece_score[piece[1]] + piece_position_score
                    if piece[0] == "b":
                        score -= self.piece_score[piece[1]] + piece_position_score

        return score


    def findRandomMove(self,valid_moves):
        """
        Picks and returns a random valid move.
        """
        return random.choice(valid_moves)



class MinimaxAgent(BaseAgent):
    def findBestMove(self,game_state, valid_moves,que,iterative = True):
        global next_move
        next_move = None
        random.shuffle(valid_moves)
        if iterative:
            for depth in range(self.DEPTH+1):
                self.Search(game_state, valid_moves, depth,
                                        1 if game_state.white_to_move else -1)
        else:
            self.Search(game_state, valid_moves, self.DEPTH,
                                        1 if game_state.white_to_move else -1)
        
        que.put(next_move)
    
    def Search(self,game_state, valid_moves, depth, turn_multiplier):
        global next_move
        if depth == 0:
            return turn_multiplier * self.EvaluateBoard(game_state)
        # move ordering - implement later //TODO
        max_score = -self.CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = -self.Search(game_state, next_moves, depth - 1, -turn_multiplier)
            if score > max_score:
                max_score = score
                if depth == self.DEPTH:
                    next_move = move
            game_state.undoMove()
        return max_score


class AlphaBetaAgent(BaseAgent):

    def findBestMove(self,game_state, valid_moves,que,iterative = True):
        global next_move
        next_move = None
        random.shuffle(valid_moves)
        if iterative:
            for depth in range(self.DEPTH+1):
                self.Search(game_state, valid_moves, depth,-self.CHECKMATE, self.CHECKMATE,
                                        1 if game_state.white_to_move else -1)
        else:
            self.Search(game_state, valid_moves, self.DEPTH, -self.CHECKMATE, self.CHECKMATE,
                                        1 if game_state.white_to_move else -1)
        
        que.put(next_move)

    
    def Search(self,game_state, valid_moves, depth, alpha, beta, turn_multiplier):
        global next_move
        if depth == 0:
            return turn_multiplier * self.EvaluateBoard(game_state)
        
        max_score = -self.CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = -self.Search(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
            if score > max_score:
                max_score = score
                if depth == self.DEPTH:
                    next_move = move
            game_state.undoMove()
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        return max_score
    
    
    


class KillerAgent(BaseAgent):
    def __init__(self, max_depth=3):
        super().__init__(max_depth)
        self.killer_moves = {}

    def findBestMove(self, game_state, valid_moves, que):
        global next_move        
        next_move = None
        random.shuffle(valid_moves)
        for depth in range(self.DEPTH + 1):
            self.killer_moves[depth] = None
            self.Search(game_state, valid_moves, depth, -self.CHECKMATE, self.CHECKMATE,
                        1 if game_state.white_to_move else -1)

        que.put(next_move)

    def Search(self, game_state, valid_moves, depth, alpha, beta, turn_multiplier):
        global next_move
        if depth == 0:
            return turn_multiplier * self.EvaluateBoard(game_state)

        # Move ordering with killer heuristic
        if self.killer_moves[depth] is not None:
            self.update_move_order(valid_moves, self.killer_moves[depth])

        max_score = -self.CHECKMATE
        for move in valid_moves:
            game_state.makeMove(move)
            next_moves = game_state.getValidMoves()
            score = -self.Search(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
            if score > max_score:
                max_score = score
                if depth == self.DEPTH:
                    next_move = move
                self.killer_moves[depth] = move
            game_state.undoMove()
            if max_score > alpha:
                alpha = max_score
            if alpha >= beta:
                break
        return max_score

    def update_move_order(self, valid_moves,killer_move):
        if killer_move in valid_moves:
            valid_moves.remove(killer_move)
            valid_moves.insert(0, killer_move)
            
    def reset_killer_moves(self):
        self.killer_moves = {}
        

    

        


    
        # def Search(self, game_state, valid_moves, depth, alpha, beta, turn_multiplier):
    #     global next_move
    #     if depth == 0:
    #         return turn_multiplier * self.EvaluateBoard(game_state)

    #     # # Check for killer moves at this depth
    #     # if depth in self.killer_moves:
    #     #     killer_move = self.killer_moves[depth]
    #     #     if killer_move in valid_moves:
    #     #         valid_moves.remove(killer_move)
    #     #         valid_moves.insert(0, killer_move)

    #     # Move ordering - implement later //TODO
    #     # Order the moves based on their estimated value
    #     # The moves that lead to the most valuable positions can then be prioritized.
    #     # scores = []
    #     # for move in valid_moves:
    #     #     game_state.makeMove(move)
    #     #     score = turn_multiplier * self.EvaluateBoard(game_state)
    #     #     game_state.undoMove()
    #     #     scores.append(score)

    #     # # Sort the moves in descending order of score
    #     # moves_scores = list(zip(valid_moves, scores))
    #     # moves_scores.sort(key=lambda x: x[1], reverse=True)
    #     # valid_moves = [move for move, _ in moves_scores]

    #     max_score = -self.CHECKMATE
    #     for move in valid_moves:
    #         game_state.makeMove(move)
    #         next_moves = game_state.getValidMoves()
    #         score = -self.Search(game_state, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
    #         if score > max_score:
    #             max_score = score
    #             if depth == self.DEPTH:
    #                 next_move = move
    #             # Update killer moves for this depth
    #             self.killer_moves[depth] = move
    #         game_state.undoMove()
    #         if max_score > alpha:
    #             alpha = max_score
    #         if alpha >= beta:
    #             # Store the killer move for the next iteration
    #             if depth not in self.killer_moves:
    #                 self.killer_moves[depth] = move
    #             break
    #         return max_score