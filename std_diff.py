import pandas as pd

file_path = 'predictions.xlsx'
data = pd.read_excel(file_path)

# Calculate the difference between predictions and the line
data['diff'] = data['regression_predictions_MAIN'] - data['line']

# Standardize these differences
data['std_diff'] = (data['diff'] - data['diff'].mean()) / data['diff'].std()

def get_top_players(data, initial_margin=2, increment=0.5, max_margin=10):
    margin = initial_margin
    selected_players = pd.DataFrame()

    while margin <= max_margin:
        # Filter data based on the absolute standardized difference and model pick
        filtered_data = data[(data['std_diff'].abs() >= margin) & 
                             ((data['model_pick'] == 'over') & (data['std_diff'] > 0) |
                              (data['model_pick'] == 'under') & (data['std_diff'] < 0))]

        print(f"Checking margin: {margin}, Found: {len(filtered_data)} players")  # Debug print

        if len(filtered_data) > 0:
            # Combine current found players with previous iterations
            selected_players = pd.concat([selected_players, filtered_data])
        else:
            # If no players are found in a new margin iteration, stop the loop
            print("No more players meet the criteria, stopping search.")
            break

        margin += increment

    # Remove duplicates if any and sort by absolute standardized differences
    selected_players = selected_players.drop_duplicates().sort_values(by='std_diff', key=abs, ascending=False)
    return selected_players.head(5)

top_5_players = get_top_players(data)
if not top_5_players.empty:
    print("Top 5 Players based on the criteria:")
    print(top_5_players[['player_name', 'regression_predictions_MAIN', 'line', 'model_pick']])
else:
    print("No players met the selection criteria.")
