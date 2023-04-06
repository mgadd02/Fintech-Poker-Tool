#run
import csv
import random

# Define a function to draw a winner from the remaining players
def draw_winner(remaining_players, player_dict):
    # Calculate the total worth of the remaining players
    total_worth = sum(player_dict[player] for player in remaining_players)

    # Create a list of tuples where each tuple contains a player name and their
    # corresponding probability of winning
    player_probs = [(player, player_dict[player] / total_worth) for player in remaining_players]

    # Draw a winner using the weighted probabilities
    winner = random.choices([player for player, prob in player_probs], weights=[prob for player, prob in player_probs])[0]

    return winner

def doDraw():
    # Read in the player results from the input CSV file
    with open('data/tournament_standings.csv', 'r') as f:
        reader = csv.reader(f)
        player_results = list(reader)

    # Convert the player results to a dictionary where the keys are the player names
    # and the values are their worth in dollars
    player_dict = {player: int(worth) for player, worth in player_results}

    # Draw the first winner
    remaining_players = list(player_dict.keys())
    first_winner = draw_winner(remaining_players, player_dict)

    # Remove the first winner from the list of remaining players
    remaining_players.remove(first_winner)

    # Draw the second winner
    second_winner = draw_winner(remaining_players, player_dict)

    # Remove the second winner from the list of remaining players
    remaining_players.remove(second_winner)

    # Draw the third winner (if there are enough players remaining)
    if remaining_players:
        third_winner = draw_winner(remaining_players, player_dict)
    else:
        third_winner = None
    
    #process outputs
    winners = [first_winner, second_winner, third_winner]
    writeDraw(winners)
    return winners
    
def writeDraw(top_three):
    # Write the results to the output CSV file
    with open('data/draw_results.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['first', 'second', 'third'])
        writer.writerow(top_three)