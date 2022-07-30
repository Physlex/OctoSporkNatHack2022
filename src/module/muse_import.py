import muselsl
import sys

class Stream:
    def __init__(self) -> None:
        print("Creating Stream")
        pass
    
    def connect(self) -> None:
        self.muses = muselsl.list_muses(interface=None)
        if not self.muses :
            print("Error, could not find a muse")
            return
        muselsl.stream(self.muses[0]['address'])
        print("Completed stream connection!")
        pass

if __name__ == "__main__" :
    my_stream = Stream()
    my_stream.connect()
    pass