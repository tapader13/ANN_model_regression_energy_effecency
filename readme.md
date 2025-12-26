# ANN Energy Efficiency — README

Minimal instructions to reproduce preprocessing, hyperparameter tuning, and training for the ANN regression model.

## Files (workspace)

- [data/raw/ENB2012_data.csv](data/raw/ENB2012_data.csv)
- [data/processed/energy_efficiency.csv](data/processed/energy_efficiency.csv)
- [model/](model/)
- [scaller/](scaller/)
- [src/preprocess.ipynb](src/preprocess.ipynb) — uses [`df.to_csv`](src/preprocess.ipynb) to write processed CSV
- [src/tune.ipynb](src/tune.ipynb) — contains [`build_model`](src/tune.ipynb) and [`tuner`](src/tune.ipynb) (Keras Tuner)
- [src/train.ipynb](src/train.ipynb) — uses [`loaded_params`](src/train.ipynb], builds and trains [`model`](src/train.ipynb) and saves [`scaller`](src/train.ipynb)
- [src/untitled_project/oracle.json](src/untitled_project/oracle.json)
- [src/untitled_project/tuner0.json](src/untitled_project/tuner0.json)
- [src/untitled_project/trial_0/build_config.json](src/untitled_project/trial_0/build_config.json)
- [src/untitled_project/trial_0/checkpoint.weights.h5](src/untitled_project/trial_0/checkpoint.weights.h5)
- [src/untitled_project/trial_0/trial.json](src/untitled_project/trial_0/trial.json)
- [src/untitled_project/trial_1/build_config.json](src/untitled_project/trial_1/build_config.json)
- [src/untitled_project/trial_1/checkpoint.weights.h5](src/untitled_project/trial_1/checkpoint.weights.h5)
- [src/untitled_project/trial_1/trial.json](src/untitled_project/trial_1/trial.json)
- [src/untitled_project/trial_2/build_config.json](src/untitled_project/trial_2/build_config.json)
- [src/untitled_project/trial_2/checkpoint.weights.h5](src/untitled_project/trial_2/checkpoint.weights.h5)
- [src/untitled_project/trial_2/trial.json](src/untitled_project/trial_2/trial.json)
- ... (other trials under `src/untitled_project/`)
- [tuning_params/best_hyperparameters.json](tuning_params/best_hyperparameters.json)

## Workflow (quick)

1. Preprocess

   - Open [src/preprocess.ipynb](src/preprocess.ipynb) and run to generate [data/processed/energy_efficiency.csv](data/processed/energy_efficiency.csv). The notebook renames columns and writes the CSV via [`df.to_csv`](src/preprocess.ipynb).

2. Hyperparameter tuning

   - Open [src/tune.ipynb](src/tune.ipynb). It defines [`build_model`](src/tune.ipynb) and runs `keras_tuner.RandomSearch` as [`tuner`](src/tune.ipynb). Run the tuning cells to produce best hyperparameters and save them to [tuning_params/best_hyperparameters.json](tuning_params/best_hyperparameters.json).

3. Train final model
   - Open [src/train.ipynb](src/train.ipynb). It loads [tuning_params/best_hyperparameters.json](tuning_params/best_hyperparameters.json) into [`loaded_params`](src/train.ipynb), builds and compiles the [`model`](src/train.ipynb), trains with early stopping, evaluates with `r2_score`, and saves artifacts:
     - Scaler: `scaller/scaller.pkl` (saved via `joblib.dump`) — see [`scaller`](src/train.ipynb)
     - Model: `model/model.pkl` (saved via `joblib.dump`) — see [`model`](src/train.ipynb)

## Notes

- Notebooks use absolute Windows paths (e.g. `D:\DL\ann_model_regression_energy_effecency\...`). Update paths or run from the same root to avoid path errors.
- Tuner settings: `max_trials=5` and `epochs=10` (see [src/tune.ipynb](src/tune.ipynb)). Adjust as needed.
- StandardScaler is used before tuning/training (see [src/tune.ipynb](src/tune.ipynb) and [src/train.ipynb](src/train.ipynb)).

## Quick commands

- Open notebooks in VS Code and run cells in order: preprocess → tune → train.
