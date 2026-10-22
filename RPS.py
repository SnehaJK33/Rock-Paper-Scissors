
import random

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)

    # First move: start with a random choice
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

    # Predict the opponent's next move using recent patterns
    last_moves = "".join(opponent_history)
    pattern_length = min(5, len(last_moves) - 1)
    pattern = last_moves[-pattern_length:]

    predictions = []

    for i in range(len(last_moves) - pattern_length):
        if last_moves[i:i + pattern_length] == pattern:
            next_index = i + pattern_length
            if next_index < len(last_moves):
                predictions.append(last_moves[next_index])

    if predictions:
        predicted_move = max(set(predictions), key=predictions.count)
    else:
        predicted_move = random.choice(["R", "P", "S"])

    # Play the move that beats the predicted opponent move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[predicted_move]
