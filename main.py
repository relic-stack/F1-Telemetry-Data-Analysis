import fastf1
import os


# Create Directory to store fastf1 cache
dir_cache= "data_cache"
try:
    os.mkdir(dir_cache)
    print("Directory", dir_cache, "created successfully." )
except FileExistsError:
    print("Directory", dir_cache, "already exists.")
    # pass (uncomment to remove print statement)
except PermissionError:
    print("Permission Denied: Unable to create", dir_cache, ".")
except Exception:
    print("An Error occured", Exception)


# Enable caching to specified data_cache folder
fastf1.Cache.enable_cache('data_cache')


