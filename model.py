"""
AlphaZero on Connect-4 from Scratch

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - make_empty_board
import numpy as np

def make_empty_board():
    """Return a 6x7 integer numpy array of zeros representing an empty Connect-4 board."""
    # TODO: create a 6x7 integer array of zeros and return it
    return np.zeros((6,7), dtype = int)

# Step 2 - column_top_row
def column_top_row(board, column):
    empty_rows = np.where(board[:, column] == 0)[0]
    if empty_rows.size > 0:
        return empty_rows[-1]  # Return the last (lowest) empty row
    return -1

# Step 3 - drop_piece
def drop_piece(board, column, player):
    # TODO: place `player` in the lowest empty row of `column` and return the new board
    row = column_top_row(board, column);
    if (row==-1):
        raise ValueError()
    else:
        new_board = board.copy()
        new_board[row,column] = player
        return new_board

# Step 4 - column_full
import numpy as np

def column_full(board, column):
    """Return True if `column` has no empty rows left."""
    # TODO: check whether the column can still accept a piece
    row = column_top_row(board, column)
    if (row == -1):
        return True
    return False

# Step 5 - valid_moves
def valid_moves(board):
    # TODO: return a list of column indices that still have at least one empty row
    return np.where(board[0,:] == 0)[0].tolist()

# Step 6 - four_in_a_row_horizontal
def four_in_a_row_horizontal(board):
    # TODO: scan every row for four consecutive matching non-zero pieces horizontally
    p1 = (board == 1)
    p2 = (board == 2)
    if (p1[:, :-3] & p1[:, 1:-2] & p1[:, 2:-1] & p1[:, 3:]).any():
        return 1
        
    if (p2[:, :-3] & p2[:, 1:-2] & p2[:, 2:-1] & p2[:, 3:]).any():
        return 2
        
    return 0

# Step 7 - four_in_a_row_vertical
def four_in_a_row_vertical(board):
    p1 = (board == 1)
    p2 = (board == 2)   
    
    # We need 4 slices, shifting down the rows by 1 each time
    if (p1[:-3, :] & p1[1:-2, :] & p1[2:-1, :] & p1[3:, :]).any():
        return 1
        
    if (p2[:-3, :] & p2[1:-2, :] & p2[2:-1, :] & p2[3:, :]).any():
        return 2
        
    return 0

# Step 8 - four_in_a_row_diagonal_down_right
def four_in_a_row_diagonal_down_right(board):
    # TODO: scan every down-right diagonal of the 6x7 board for four matching non-zero pieces
    for i in range (3):
        for j in range (4):
            a = board[i, j]
            b = board[i+1, j+1]
            c = board[i+2, j+2]
            d = board[i+3, j+3]
            if(a==b==c==d==1):
                return 1
            elif(a==b==c==d==2):
                return 2
    return 0

# Step 9 - four_in_a_row_diagonal_up_right
def four_in_a_row_diagonal_up_right(board):
    # Rows MUST start lower down (indices 3, 4, 5) so we can safely subtract 3
    for i in range(3, 6):
        # Columns start at the left (indices 0, 1, 2, 3) so we can safely add 3
        for j in range(4):
            a = board[i, j]
            b = board[i-1, j+1]  # Up 1, Right 1
            c = board[i-2, j+2]  # Up 2, Right 2
            d = board[i-3, j+3]  # Up 3, Right 3
            
            if a == b == c == d == 1:
                return 1
            elif a == b == c == d == 2:
                return 2
                
    return 0

# Step 10 - check_winner (not yet solved)
# TODO: implement

# Step 11 - board_is_full (not yet solved)
# TODO: implement

# Step 12 - is_terminal (not yet solved)
# TODO: implement

# Step 13 - other_player (not yet solved)
# TODO: implement

# Step 14 - step_env (not yet solved)
# TODO: implement

# Step 15 - encode_board (not yet solved)
# TODO: implement

# Step 16 - board_to_torch_tensor (not yet solved)
# TODO: implement

# Step 17 - init_conv_backbone (not yet solved)
# TODO: implement

# Step 18 - init_policy_head (not yet solved)
# TODO: implement

# Step 19 - init_value_head (not yet solved)
# TODO: implement

# Step 20 - build_policy_value_net (not yet solved)
# TODO: implement

# Step 21 - policy_value_forward (not yet solved)
# TODO: implement

# Step 22 - action_mask (not yet solved)
# TODO: implement

# Step 23 - masked_policy_logits (not yet solved)
# TODO: implement

# Step 24 - masked_log_softmax (not yet solved)
# TODO: implement

# Step 25 - sample_action_from_policy (not yet solved)
# TODO: implement

# Step 26 - greedy_action_from_policy (not yet solved)
# TODO: implement

# Step 27 - make_mcts_node (not yet solved)
# TODO: implement

# Step 28 - node_q_value (not yet solved)
# TODO: implement

# Step 29 - ucb_score (not yet solved)
# TODO: implement

# Step 30 - select_best_child (not yet solved)
# TODO: implement

# Step 31 - select_leaf (not yet solved)
# TODO: implement

# Step 32 - evaluate_with_network (not yet solved)
# TODO: implement

# Step 33 - expand_node (not yet solved)
# TODO: implement

# Step 34 - backup_value (not yet solved)
# TODO: implement

# Step 35 - run_one_simulation (not yet solved)
# TODO: implement

# Step 36 - run_mcts (not yet solved)
# TODO: implement

# Step 37 - visit_count_policy (not yet solved)
# TODO: implement

# Step 38 - mcts_choose_action (not yet solved)
# TODO: implement

# Step 39 - record_self_play_step (not yet solved)
# TODO: implement

# Step 40 - play_self_play_game (not yet solved)
# TODO: implement

# Step 41 - assign_value_targets (not yet solved)
# TODO: implement

# Step 42 - generate_self_play_batch (not yet solved)
# TODO: implement

# Step 43 - value_loss_mse (not yet solved)
# TODO: implement

# Step 44 - policy_loss_cross_entropy (not yet solved)
# TODO: implement

# Step 45 - l2_regularization_loss (not yet solved)
# TODO: implement

# Step 46 - combined_loss (not yet solved)
# TODO: implement

# Step 47 - encode_batch_states (not yet solved)
# TODO: implement

# Step 48 - iterate_minibatches (not yet solved)
# TODO: implement

# Step 49 - training_step (not yet solved)
# TODO: implement

# Step 50 - training_epoch (not yet solved)
# TODO: implement

# Step 51 - self_play_iteration (not yet solved)
# TODO: implement

# Step 52 - train_loop (not yet solved)
# TODO: implement

# Step 53 - random_policy_action (not yet solved)
# TODO: implement

# Step 54 - greedy_agent_action (not yet solved)
# TODO: implement

# Step 55 - play_one_match (not yet solved)
# TODO: implement

# Step 56 - match_win_rate (not yet solved)
# TODO: implement

# Step 57 - evaluate_against_random (not yet solved)
# TODO: implement

