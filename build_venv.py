from distutils.command.build import build
import subprocess
import sys

class Build:
    def __init__(self) -> None:
        print("Creating build environment...")
        pass

    def create_venv(self) -> None:
        args = [
            "python3",
            "-m",
            "venv",
            "environment"
        ]
        subprocess.Popen(args)
        pass

#### START OF MAIN ###
if __name__ == "__main__" :
    builder = Build()
    builder.create_venv()
    pass
