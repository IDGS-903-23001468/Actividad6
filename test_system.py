import subprocess
import sys


def test_sistema_correcto():
    resultado = subprocess.run(
        [sys.executable, "main.py"],
        input="100\n10\n",
        capture_output=True,
        text=True
    )

    assert "104.4" in resultado.stdout


def test_sistema_error():
    resultado = subprocess.run(
        [sys.executable, "main.py"],
        input="hola\n10\n",
        capture_output=True,
        text=True
    )

    assert "Error" in resultado.stdout
    assert resultado.returncode == 0