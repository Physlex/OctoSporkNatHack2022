from ast import Pass
import subprocess
from matplotlib.pyplot import connect

from numpy import record

class Command :
    def __init__(self) -> None:
        print("Executing command")
        pass

    def execute() -> None:
        pass

class Connect(Command) :
    def __init__(self) -> None:
        super().__init__()
        pass

    def execute(self) -> None:
        args = ["python3", "./src/server/data/connect.py"]
        subprocess.Popen(args)    
        pass

if __name__ == "__main__" :
    connect_muse = Connect()
    connect_muse.execute()
    pass