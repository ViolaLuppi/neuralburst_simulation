"""Save NeuroDSP-style figures for the raw signal and detected bursts."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from neurodsp.plts.time_series import plot_time_series, plot_bursts


def main():
    """Create and save figures."""

    data = pd.read_csv("results/burst_detection.csv")

    times = data["time_s"].to_numpy()
    signal = data["signal"].to_numpy()
    bursting = data["detected_burst"].astype(bool).to_numpy()

    Path("figures").mkdir(exist_ok=True)

    # Figure 1: raw simulated signal
    plot_time_series(
        times,
        signal,
        xlabel="Time (s)",
        ylabel="Amplitude",
        title="Simulated neural signal",
        figsize=(15, 3),
    )

    plt.savefig(
        "figures/raw_signal.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    # Figure 2: signal with detected bursts
    plot_bursts(
        times,
        signal,
        bursting,
        labels=["Simulated signal", "Detected beta burst"],
        figsize=(15, 3),
    )

    plt.savefig(
        "figures/burst_detection.png",
        dpi=300,
        bbox_inches="tight",
    )
    plt.close()

    print("Saved figures:")
    print(" - figures/raw_signal.png")
    print(" - figures/burst_detection.png")


if __name__ == "__main__":
    main()