import muselsl
import sys

class Muse:
    def __init__(self, ID) -> None:
        """
        # Finds a muse in order of connection
        """
        print("Searching for muses")
        self.muses = muselsl.list_muses(interface=None)
        if not self.muses :
            print("Error, could not find a muse")
            return

        if (len(self.muses) < ID) :
            print("""Error, access violation of muse list
            ID too big.""")
        self.muse = self.muses[ID]
        self.muses
        self.address = self.muse["address"]
        self.name = self.muse["name"]
        self.ID = ID
        pass
    
    def connect(self) -> None:
        print(f"Connecting muse: {self.name, self.ID} at: {self.address}")
        muselsl.stream(self.address)
        pass

    def record(self):
        muselsl.record()
        pass  # TODO(Alexander): Return and save CSV format of data

if __name__ == "__main__" :
    myMuse = Muse(0)
    myMuse.connect()
    pass
