import pytest
import math
from render import dynamic_resolution as mod

CASES = [
    ("proj", 'm.proj(2, 0.5) == 4'),
    ("ui", 'm.ui(0.5) == 1.0'),
    ("smooth", 'm.smooth(10, 20, 0.5) == 15'),
    ("step", 'm.step(0.5, 1, 0.2) == approx(0.7)'),
    ("band", 'm.band(0.8, 0.5, 1) is True'),
    ("reproject", 'm.reproject((0.5, 0.5), (0.1, 0.2)) == (0.6, 0.7)'),
    ("taa", 'm.taa(1, 0.5) == 0.5'),
    ("bloom", 'm.bloom(2, 0.5) == 1'),
    ("sharpen", 'm.sharpen(2, 0.5) == 4'),
    ("cam", 'm.per_cam(1) == "res:1"'),
    ("res", 'm.res(1920, 0.5) == 960'),
    ("pct", 'm.pct(1920, 960) == approx(0.5)'),
    ("clamp", 'm.clamp_scale(0.3) == 0.5'),
    ("fps", 'm.fps(16.6) == approx(60.24, abs=0.1)'),
    ("key", 'm.key(2) == "cam:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
