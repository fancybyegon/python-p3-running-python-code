from os import path

def test_app_py_exists():
    assert path.exists("lib/app.py")

def test_app_py_prints_expected_output():
    import subprocess
    result = subprocess.run(["python", "lib/app.py"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello World! Pass this test, please."