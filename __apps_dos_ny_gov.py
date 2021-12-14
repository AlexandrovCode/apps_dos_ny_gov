import time
import json
from apps_dos_ny_gov import *

if __name__ == '__main__':
    start_time = time.time()

    a = Handler()

    final_data = a.Execute('10 EXPONENT 13 BANK & AIRLINE INVESTMENT CORPORATION', '', '', '')
    print(json.dumps(final_data, indent=4))

    elapsed_time = time.time() - start_time
    print('\nTask completed - Elapsed time: ' + str(round(elapsed_time, 2)) + ' seconds')
