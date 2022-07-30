import muselsl
import sys

class Stream:
    def __init__(self) -> None:
        print("Creating Stream")
        pass
    
    def connect(self) -> None:
        """
        # Connect to the first LAN based BT muse avaliable, then start streaming from it.
        """
        self.muses = muselsl.list_muses(interface=None)
        if not self.muses :
            print("Error, could not find a muse")
            return
        muselsl.stream(self.muses[0]['address'])
        print("Completed stream connection!")
        pass
