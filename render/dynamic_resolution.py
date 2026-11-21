import math

def proj(base, scale):
    """同步投影。"""
    raise NotImplementedError("TODO: proj")

def ui(scale):
    """UI 独立目标。"""
    raise NotImplementedError("TODO: ui")

def smooth(prev, cur, alpha):
    """平滑帧时间。"""
    raise NotImplementedError("TODO: smooth")

def step(cur, target, max_step):
    """小步进。"""
    raise NotImplementedError("TODO: step")

def band(value, lo, hi):
    """滞回区间。"""
    raise NotImplementedError("TODO: band")

def reproject(uv, delta):
    """历史重投影。"""
    raise NotImplementedError("TODO: reproject")

def taa(base, scale):
    """TAA 按比例。"""
    raise NotImplementedError("TODO: taa")

def bloom(base, scale):
    """后处理按比例。"""
    raise NotImplementedError("TODO: bloom")

def sharpen(strength, scale):
    """锐化补偿。"""
    raise NotImplementedError("TODO: sharpen")

def per_cam(camera_id):
    """按相机独立。"""
    raise NotImplementedError("TODO: per_cam")

def res(width, scale):
    """分辨率计算。"""
    raise NotImplementedError("TODO: res")

def pct(native, current):
    """比例。"""
    raise NotImplementedError("TODO: pct")

def clamp_scale(scale):
    """缩放钳制。"""
    raise NotImplementedError("TODO: clamp_scale")

def fps(frame_ms):
    """帧率。"""
    raise NotImplementedError("TODO: fps")

def key(camera_id):
    """相机键。"""
    raise NotImplementedError("TODO: key")
