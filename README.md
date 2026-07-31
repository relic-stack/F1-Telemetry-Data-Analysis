# F1-Telemetry-Data-Analysis


## Progress

Fixed issue with compatability with crytography wheel, it was failing as the venv i created kept using python 3.13 which doesnt support arm wheel for crytpography. During virtual env creation, i had to specify python version. However, this is after installing the 64 bit emulated version.

Next step is to verify im still using arm version of python 3.12 and not the emulated 64bit. Also test if i can remove requirements.txt and try installing fastf1 on 3.12.9 without it with no errors.