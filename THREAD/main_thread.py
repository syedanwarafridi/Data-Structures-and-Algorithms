"""
WHEN EVER WE RUN A PROGRAM. PYTHON INTERPRETER WILL REQUEST TO OS FOR CREATING A THREAD.
THE DEFAULD THREAD WHICH WILL BE CREATED THROUGH OS WILL BE CALLED MAIN THREAD.
"""

import threading

print(threading.currentThread().is_alive())