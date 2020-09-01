import os
import sys
import time
"""
 * Imports of your controllers
"""

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

start_time = time.time()

from routes.router import Router


try:
    route = Router()
    route.DEFAULT_ROUTE
finally:
    print("--- %s seconds ---" % (time.time() - start_time))
