# F1 Telemetry Data Analysis
 
A data analysis project using [FastF1](https://github.com/theOehrly/Fast-F1) to explore Formula 1 telemetry and session data in Python.
 
## Overview
 
## Setup
  
## Troubleshooting / Setup Issues
 
### `cryptography` wheel build failure on ARM64 Windows
 
**Issue:** `pip install fastf1` fails on native ARM64 Windows Python (tested on 3.11 and 3.12.9, both ARM builds) with a wheel build error for `cryptography`, a transitive dependency.
 
**Root cause:** The `cryptography` package does not currently publish a prebuilt wheel for `win_arm64` on PyPI (the Python Package Index — the official repository pip installs packages from). This forces pip to build the package from source, which requires a correctly configured Rust toolchain and an ARM64-native OpenSSL build, neither of which is available by default on Windows ARM64. This is a known, unresolved upstream issue and not specific to this project or Python version.
 
Tracking issue: https://github.com/pyca/cryptography/issues/14249
 
An earlier troubleshooting step also confirmed the virtual environment was inadvertently created against an emulated x86-64 Python interpreter rather than the native ARM64 build — installing under emulation avoided the error, which confirmed the failure was architecture-specific rather than a project configuration problem.
 
**Planned resolution:** Migrate the development environment to **WSL2** (Windows Subsystem for Linux 2) running an ARM64 Ubuntu distribution. WSL2 runs a native ARM64 Linux environment (no x86 emulation), and `cryptography` already publishes prebuilt `manylinux_aarch64` wheels for Linux ARM64, which should allow `fastf1` to install cleanly with no source build required. VS Code can connect to the WSL2 environment via the Microsoft WSL extension, preserving the normal editing experience.
 
**Status:** Root cause identified. WSL2 migration planned but not yet implemented.
 
## Progress
 
See [PROGRESS.md](./PROGRESS.md) for a dated log of development progress and decisions.