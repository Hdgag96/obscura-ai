import pandas as pd


def load_logs(file_path: str) -> pd.DataFrame:
    """
    Load security logs from a CSV file.
    """
    try:
        logs = pd.read_csv(file_path)
        return logs
    except FileNotFoundError:
        raise FileNotFoundError(f"Log file not found: {file_path}")
    