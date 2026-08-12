import fastf1
import os


# Set log level to warning (Order: DEBUG, INFO, WARNING, ERROR and CRITICAL)
fastf1.set_log_level('WARNING')


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


# Session Loader Function
def load_session(year, event, session_type):
    session = fastf1.get_session(year, event, session_type)
    session.load()
    return session.results.columns, session.results

example_session = load_session(2021, 7, 'Q')
print(example_session)