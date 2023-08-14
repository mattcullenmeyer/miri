import pandas as pd 
import time
import threading

# https://realpython.com/intro-to-python-threading/
# https://superfastpython.com/thread-long-running-background-task/
def watch_df():
  global df
  last_seen = df
  while True:
    if not df.equals(last_seen):
      print(f'df has changed to {df.to_json(orient="table")}')
      last_seen = df
    time.sleep(1)

data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data)

thread = threading.Thread(target=watch_df, daemon=True)
thread.start()

print(df)
