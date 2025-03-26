import os
import json

def debug_config():
    # Print the current working directory
    print("Current working directory:", os.getcwd())

    # Build the absolute path to config.json
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, "config.json")
    print("Expected config.json path:", config_path)

    # Check if the file exists
    if not os.path.exists(config_path):
        print("Error: 'config.json' not found at the expected path.")
        return

    # Try to open and load the file
    try:
        with open(config_path, "r") as file:
            config = json.load(file)
        print("Successfully loaded config.json!")
        print("Contents of config.json:", config)
    except json.JSONDecodeError:
        print("Error: 'config.json' contains invalid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the debug function
if __name__ == "__main__":
    debug_config()