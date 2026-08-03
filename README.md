# F1-Telemetry-Data-Analysis


## Progress

Fixed issue with compatibility for the cryptography wheel, it was failing because the venv I created kept using Python 3.13, which doesn't support Arm wheel for cryptography. During virtual env creation, I had to specify the Python version. However, this is after installing the 64-bit emulated version.

Next step is to verify I'm still using Arm version of Python 3.12 and not the emulated 64bit. Also test if I can remove requirements.txt and try installing fastf1 on 3.12.9 without it with no errors. If this works due to using 3.12.9 64-bit, then this is only a workaround to the bug and not a fix.

03/08/26
Verified the venv is using the 64bit version.