# újévi visszaszámláló
#\r carriage returnt nem tudja kezelni futtatáskor, de terminálban működik
# újabb print while-ból kilépve (indent már nincs!)

import time
from datetime import datetime

new_year = datetime(year=2021, month=1, day=1, hour=0, minute=0, second=0)

def countdown_till_2021(no_of_counts):

    while no_of_counts:
        system_time = datetime.now()
        delta_from_now = new_year - system_time
        print(delta_from_now, end='\r')
        time.sleep(1)
        no_of_counts -= 1
    print('               Goodbye!\n')


countdown_till_2021(10)


