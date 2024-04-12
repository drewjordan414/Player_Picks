# # #Absoulte differnce
import pandas as pd

file_path = 'predictions.xlsx'  
data = pd.read_excel(file_path)

def get_top_players(data, initial_margin=2, increment=2):
    margin = initial_margin
    selected_players = pd.DataFrame()

    while len(selected_players) < 5:
        # Filter players based on the margin
        filtered_data = data[(data['model_pick'] == 'over') & (data['regression_predictions_MAIN'] - data['line'] >= margin) |
                             (data['model_pick'] == 'under') & (data['line'] - data['regression_predictions_MAIN'] >= margin)]
        if len(filtered_data) >= 5:
            selected_players = filtered_data.sort_values(by='regression_predictions_MAIN', ascending=False).head(5)
            break
        margin += increment

    return selected_players

top_5_players = get_top_players(data)
print("Top 5 Players based on the criteria:")
print(top_5_players[['player_name', 'regression_predictions_MAIN', 'line', 'model_pick']])
