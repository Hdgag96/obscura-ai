def analyze_threat(row):

    severity = row.get("severity", "Unknown")
    event_type = row.get("event_type", "Unknown Event")
    source_ip = row.get("source_ip", "Unknown IP")

    return (
        f"{severity} severity threat detected involving "
        f"{event_type} from {source_ip}."
    )
