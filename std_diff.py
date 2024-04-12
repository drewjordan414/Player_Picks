import pandas as pd

file_path = 'predictions.xlsx'  
data = pd.read_excel(file_path)

# Calculate standardized differences ahead of the loop
data['std_diff_over'] = ((data['regression_predictions_MAIN'] - data['line']) - data['regression_predictions_MAIN'].mean()) / data['regression_predictions_MAIN'].std()
data['std_diff_under'] = ((data['line'] - data['regression_predictions_MAIN']) - data['regression_predictions_MAIN'].mean()) / data['regression_predictions_MAIN'].std()

def get_top_players(data, initial_margin=2, increment=0.5):
    margin = initial_margin
    selected_players = pd.DataFrame()

    while len(selected_players) < 5:
        # Use pre-calculated standardized differences
        filtered_data = data[((data['model_pick'] == 'over') & (data['std_diff_over'] >= margin)) |
                             ((data['model_pick'] == 'under') & (data['std_diff_under'] >= margin))]
        
        if len(filtered_data) >= 5:
            selected_players = filtered_data.sort_values(by='regression_predictions_MAIN', ascending=False).head(5)
            break
        margin += increment

    return selected_players

top_5_players = get_top_players(data)
print("Top 5 Players based on the criteria:")
print(top_5_players[['player_name', 'regression_predictions_MAIN', 'line', 'model_pick']])
