import muselsl

class NatMuse:
    def __init__(self) -> None:
        pass
    
    def connect(self, ID) -> None:
        print("Searching for muses")
        self.muses = muselsl.list_muses(interface=None)
        if not self.muses :
            print("Error, could not find a muse")
            return

        if (len(self.muses) < ID) :
            print("""Error, access violation of muse list
            ID too big.""")
        self.ID = ID

        self.muse = self.muses[self.ID]
        self.address = self.muse["address"]
        self.name = self.muse["name"]

        print(f"Connecting muse: {self.name, self.ID} at: {self.address}")
        muselsl.stream(self.address)
        pass

    def record(self, duration):
        muselsl.record(duration, filename='recording')
        pass  # TODO(Alexander): Return and save CSV format of data
