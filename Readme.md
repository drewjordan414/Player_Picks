# Top Player Picks Analysis

This Python script suite includes `std_diff.py` and `abs_diff.py`, which analyze player prediction data from a LightGBM regressor and quantile model to determine the top 5 basketball player picks. `std_diff.py` focuses on standardized differences between predicted points and a specified "line," using dynamic margins to isolate the best candidates. Conversely, `abs_diff.py` utilizes absolute differences to perform a similar analysis, ensuring a robust selection process in both methods. Each script employs a distinct approach to filtering and selecting players based on their predicted performances, providing versatile tools for sports analytics.


## Features

- **Standardized Difference Calculation:** Calculates the difference between each player's predicted performance and a "line", standardizing these differences to focus on significant deviations.
- **Dynamic Margin Filtering:** Begins with a 2-point margin and incrementally increases by 0.5 points. The search stops when no more players meet the increasing margin criteria or when the margin exceeds 10 points.
- **Model Pick Alignment:** Considers the model's "over" or "under" pick, ensuring that selections align with predictive insights.
- **Output Information:** Outputs the player's name, predicted points, the line, and whether the pick is 'over' or 'under' for those who meet the selection criteria.

## Requirements

To run this script, ensure Python is installed on your system along with the following Python libraries:
- `pandas`
- `openpyxl` (for handling Excel files)

Install these dependencies via pip:
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
   python std_diff.py
   ```
   or 

   ```bash
   python abs_diff.py
   ```

