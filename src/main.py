from utils.path_utils import get_project_root
from features.feature_a import fetch_data
from utils import os_utils

def main():
    print("========== Python processing ==========")

    print(f"Project root: {get_project_root()}")
    print(f"OS: {os_utils.get_os()}")

    url = "https://www.example.com"
    print(f"Getting data from {url}...")
    data = fetch_data(url)
    print("Part of data：")
    print(data)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("========== End of Python ==========")
        input("\nPress Enter to exit...")
