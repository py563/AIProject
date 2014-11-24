

import web

web.config.debug = False
db = web.database(dbn='sqlite', db='Mydata.db')
DISPLAY_CANDIDATES = True

