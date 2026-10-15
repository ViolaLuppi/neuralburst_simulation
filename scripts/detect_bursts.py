"""Detect beta bursts in the simulated neural signal."""

from pathlib import Path

import pandas as pd

from neurodsp.burst import detect_bursts_dual_threshold, compute_burst_stats


# Burst detection settings
FS = 1000
BETA_RANGE = (13, 30)
DUAL_THRESHOLD = (1, 2)


def main():
    """Detect beta bursts and save burst results."""

    # Load simulated signal
    data = pd.read_csv("data/simulated_signal.csv")
    signal = data["signal"].to_numpy()

    # Detect beta bursts
    bursting = detect_bursts_dual_threshold(
        signal,
        FS,
        DUAL_THRESHOLD,
        BETA_RANGE,
    )

    # Compute summary statistics
    burst_stats = compute_burst_stats(
        bursting,
        FS,
    )

    # Create results directory if needed
    Path("results").mkdir(exist_ok=True)

    # Save burst detection for every time point
    data["detected_burst"] = bursting.astype(int)

    data.to_csv(
        "results/burst_detection.csv",
        index=False,
    )

    # Save summary statistics
    pd.DataFrame([burst_stats]).to_csv(
        "results/burst_statistics.csv",
        index=False,
    )

    # Print statistics
    print("Burst detection complete:")
    for key, value in burst_stats.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()