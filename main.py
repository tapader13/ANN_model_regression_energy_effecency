import subprocess
import sys

# list of steps to run (name, script path)
STEPS = [
    ("Preprocessing", "src/preprocess.ipynb"),
    ("Tuning hyperperameter", "src/tune.ipynb"),
    ("Training Model", "src/train.ipynb"),
]

def run_script(name, script_path):
    print("\n" + "="*50)
    print(f"Running Step: {name}")
    print("="*50)
    try:
        subprocess.run([sys.executable, script_path], check=True)
    except subprocess.CalledProcessError:
        print(f"Step '{name}' failed. Stopping pipeline.")
        sys.exit(1)
    print(f"Step '{name}' completed!")

print("Starting ANN Pipeline...")

for step_name, script_file in STEPS:
    run_script(step_name, script_file)

print("\nANN Pipeline finished successfully!")
