from subprocess import run
from pathlib import Path
import difflib
import yaml
import torch

def test_conda_environment():
    """Compares output of ``conda env export`` with the contents of ``conda_env.yml``. """

    # execute 'conda env export' and parse yaml output:
    cmd_result = run(['conda', 'env', 'export'], capture_output=True)
    d0 = yaml.safe_load(cmd_result.stdout.decode('utf-8'))

    # read saved conda environment from yaml file:
    current_file_path = Path(__file__)
    fn = current_file_path.parent.parent / 'conda_env.yml'
    print(f"Yaml file is located at: {fn}")
    with open(fn, 'rt') as fp:
        d1 = yaml.safe_load(fp)
    
    # Compare the two dictionaries:
    if d0['channels'] != d1['channels']:
        print(f"Conda channels differ (current vs '{fn}'): " +
              f"{d0['channels']} vs {d0['channels']}")

    s0, s1 = sorted(d0['dependencies']), sorted(d1['dependencies'])
    if s0 != s1:
        df = difflib.Differ()
        ds = df.compare(s0, s1)
        ts = f"Differences of current environment (+) and file '{fn}' (-):"
        print("\n" + ts)
        print('=' * len(ts))
        print('\n'.join(l_ for l_ in ds if not l_.startswith(' ')))
        assert False  # fail test

    print("Test passed. You are on the most up-to-date conda virtual env for SushiGo")

if __name__ == "__main__":
    test_conda_environment()