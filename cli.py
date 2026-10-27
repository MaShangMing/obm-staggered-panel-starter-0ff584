import json
import sys
from estimator import estimate

if __name__ == "__main__":
    panel = json.load(sys.stdin)
    json.dump({"effects": estimate(panel)}, sys.stdout, allow_nan=False)
    sys.stdout.write(chr(10))
