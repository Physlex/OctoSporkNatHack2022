from asyncio import subprocess
from cProfile import run
from command import Command
import subprocess

class Run(Command) :
    def __init__(self) -> None:
        super().__init__()

    def execute(self) -> None:
        args = ["python3", "./src/server/data/app.py"]
        subprocess.Popen(args)
        pass

if __name__ == "__main__" :
    run_command = Run()
    run_command.execute()
    pass
