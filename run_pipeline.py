"""Run the complete neural burst analysis pipeline."""

import subprocess
import sys


SCRIPTS = [
    "scripts/simulate_data.py",
    "scripts/detect_bursts.py",
    "scripts/make_figure.py",
]


def main():
    """Run all analysis steps in order."""

    for script in SCRIPTS:
        print(f"\nRunning {script}...")
        subprocess.run(
            [sys.executable, script],
            check=True,
        )

    print("\nPipeline completed successfully.")


if __name__ == "__main__":
    main()