import pandas as pd

file_path = 'predictions_5.xlsx'
data = pd.read_excel(file_path)
data['diff'] = data['regression_predictions_mean'] - data['line']
data['std_diff'] = (data['diff'] - data['diff'].mean()) / data['diff'].std()

def get_top_players(data, initial_margin=2, increment=0.5, max_margin=10):
    margin = initial_margin
    selected_players = pd.DataFrame()

    while margin <= max_margin:
        filtered_data = data[(data['std_diff'].abs() >= margin) & 
                             ((data['model_pick'] == 'over') & (data['std_diff'] > 0) |
                              (data['model_pick'] == 'under') & (data['std_diff'] < 0))]

        print(f"Checking margin: {margin}, Found: {len(filtered_data)} players")  # Debug print

        if len(filtered_data) > 0:
            selected_players = pd.concat([selected_players, filtered_data])
        else:
            print("No more players meet the criteria, stopping search.")
            break

        margin += increment
    selected_players = selected_players.drop_duplicates().sort_values(by='std_diff', key=abs, ascending=False)
    return selected_players.head(5)

top_5_players = get_top_players(data)
if not top_5_players.empty:
    print("Top 5 Players based on the criteria:")
    print(top_5_players.rename(columns={
        'player_name': 'Player Name',
        'regression_predictions_mean': 'Prediction',
        'model_pick': 'Pick'
    })[['Player Name', 'Prediction', 'Pick']])
else:
    print("No players met the selection criteria.")
