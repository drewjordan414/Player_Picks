# Top Player Picks Analysis

This Python script analyzes player prediction data from a LightGBM regressor and quantile model to determine the top 5 basketball player picks. The selection is based on the predicted points relative to a specified "line," with dynamic margins used to filter the best candidates.

## Features

- **Dynamic Margin Filtering:** Starts with a 2-point margin between predicted points and the line, incrementally increasing by 2 points until 5 players are selected.
- **Model Alignment:** Considers players whose predictions are either above or below the line as specified by the model's "over" or "under" pick.
- **Output Information:** Displays the player's name, predicted points, the line, and the model's pick (over/under).

## Requirements

To run this script, you'll need Python installed on your system along with the following Python libraries:
- `pandas`
- `openpyxl` (for handling Excel files)

You can install these dependencies via pip:
```bash
pip install pandas openpyxl

```

## Usage

1. **Data Input**: Ensure your Excel file containing the player data is named 'predictions.xlsx' and is located in the same directory as the script. The data should include the following columns:
   - `player_name`: Name of the player.
   - `player_team`: Team of the player.
   - `line`: Benchmark or target score.
   - `team_abbreviation`: Abbreviated name of the team.
   - `opponent`: Opponent team.
   - `regression_predictions_0.25`: 25th percentile prediction from the regression model.
   - `regression_predictions_0.5`: Median (50th percentile) prediction.
   - `regression_predictions_0.75`: 75th percentile prediction.
   - `regression_predictions_MAIN`: Main prediction from the regression model.
   - `model_pick`: Model's decision (e.g., "over" or "under").

2. **Run the Script**: Execute the script in your Python environment. Ensure you are in the directory containing the script and run:
   ```bash
   python picks.py

