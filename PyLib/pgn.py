'''IEC 61162-3, is a plug-and-play communications standard used for connecting marine sensors and display units
within ships and boats.
NMEA 2000, abbreviated to NMEA2k or N2K
'''



class NMEA2000Packet(object):
    def __init__(self, **kw):
        self.pgn = kw.get('pgn',0)
        super(NMEA2000Packet, self).__init__()
