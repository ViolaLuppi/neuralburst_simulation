"""Simulate neural activity containing transient beta bursts."""

import pandas as pd

from neurodsp.sim import sim_combined
from neurodsp.utils import create_times, set_random_seed


# Simulation settings
FS = 1000
N_SECONDS = 10
BETA_FREQUENCY = 20

# Make simulation reproducible
set_random_seed(42)

# Define signal components
components = {
    "sim_synaptic_current": {
        "n_neurons": 1000,
        "firing_rate": 2,
        "t_ker": 1.0,
        "tau_r": 0.002,
        "tau_d": 0.02,
    },
    "sim_bursty_oscillation": {
        "freq": BETA_FREQUENCY,
        "enter_burst": 0.2,
        "leave_burst": 0.2,
    },
}

# Simulate signal
signal = sim_combined(
    N_SECONDS,
    FS,
    components,
)

# Create time vector
times = create_times(
    N_SECONDS,
    FS,
)

# Save simulated data
data = pd.DataFrame(
    {
        "time_s": times,
        "signal": signal,
    }
)

data.to_csv(
    "data/simulated_signal.csv",
    index=False,
)

print("Saved simulated signal to data/simulated_signal.csv")