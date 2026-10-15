# Neural Burst Simulation

A reproducible Python pipeline for simulating neural activity with transient beta bursts, detecting the bursts with NeuroDSP (`neurodsp-tools.github.io`), and visualizing the results.

NeuroDSP is a toolbox for digital signal processing of neural time series. It also includes simulation tools for generating plausible simulations of neural time series.

## Purpose

The project demonstrates an analysis workflow for neural burst detection using simulated data.

The simulated signal contains an aperiodic component and transient 20 Hz beta activity. Beta bursts are detected in the 13–30 Hz range using NeuroDSP's dual-threshold method.

## Workflow

```text
Simulate neural signal
        ↓
Detect beta bursts
        ↓
Calculate burst statistics
        ↓
Generate figures
```

## Dependencies

- Python 3.13
- NeuroDSP 2.3.0 (`neurodsp-tools.github.io`)
- pandas
- matplotlib

Install the required packages with:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the complete analysis from the repository root:

```bash
python run_pipeline.py
```

The pipeline produces:

```text
data/simulated_signal.csv
results/burst_detection.csv
results/burst_statistics.csv
figures/raw_signal.png
figures/burst_detection.png
```

## Scripts

- `scripts/simulate_data.py` — simulates neural activity containing transient beta bursts.
- `scripts/detect_bursts.py` — detects beta bursts and calculates burst statistics.
- `scripts/make_figure.py` — generates figures of the raw signal and detected bursts.
- `run_pipeline.py` — runs the complete workflow in the correct order.

## Results

With the current simulation parameters:

- 5 beta bursts were detected
- mean burst duration: 0.455 s
- time spent in bursts: 22.74%
- burst rate: 0.5 bursts/s

## Reproducibility

The workflow uses a fixed random seed, separate scripts for individual analysis steps, saved intermediate results, a project-specific Python environment, and Git for version control.

## Reference

- NeuroDSP — *Burst Detection* tutorial (`neurodsp-tools.github.io`)  
  https://neurodsp-tools.github.io/neurodsp/auto_tutorials/burst/plot_BurstDetection.html