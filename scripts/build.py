import os
import subprocess


def compile_with_pyinstaller(script: str, args=None):
    command = ["pyinstaller", script, "--onefile", "--noconfirm"]
    if args:
        command += args
    print(f"Running pyinstaller: {command}")
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("Error running pyinstaller:")
        print(result.stderr)
    else:
        print("Pyinstaller finished successfully!")
        print(result.stdout)


def build_executable():
    print("Building executable...")
    script = os.path.join("nexus", "main.py")
    compile_with_pyinstaller(script)


def build_installer():
    print("Building installer...")
