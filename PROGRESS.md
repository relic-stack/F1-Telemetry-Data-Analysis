# Progress Log
 
## 03/08/2026
 
- Diagnosed `cryptography` wheel build failure when installing `fastf1` in a virtual environment.
- Traced the cause to the virtual environment being created against an emulated x86-64 Python interpreter rather than the intended native ARM64 build; explicitly specifying the Python version during venv creation was required.
- Confirmed the issue is a known upstream limitation (no `win_arm64` wheel for `cryptography`), not a local configuration bug — see [README: Troubleshooting](./README.md#troubleshooting--setup-issues).
- Verified the virtual environment was running the emulated 64-bit interpreter, not native ARM64.
- Decided next step: migrate development environment to WSL2 (Ubuntu ARM64) for native ARM Python with working `cryptography` wheels.

## 05/08/2026
- Installed and initialised WSL2 (Ubuntu ARM64) to resolve the package build issue from earlier.
- Reinstalled native ARM64 VS Code to resolve crashing on app launch and connected it to the WSL environment.
- Cloned Github repo into Linux home filesystem
- Created project venv named: `fastf1-venv`, installed fastf1 and mapped VS Code interpreter to venv.
- Added `fastf1-env/` to .gitignore to prevent virtual env files from being tracked by git.

