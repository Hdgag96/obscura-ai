def detect_threats(logs):

    suspicious_logs = logs[
        (logs["event_type"].str.contains("failed login", case=False, na=False)) |
        (logs["event_type"].str.contains("powershell", case=False, na=False)) |
        (logs["severity"].str.lower().isin(["high", "critical"]))
    ]
    return suspicious_logs