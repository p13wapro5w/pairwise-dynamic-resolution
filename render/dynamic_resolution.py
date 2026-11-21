import math

def proj(base, scale):
    """同步投影：渲染目标缩放后，投影矩阵按 1/scale 补偿，避免画面拉伸。"""
    return base / scale

def ui(scale):
    """UI 独立目标：UI 始终按原生分辨率渲染，不随 3D 缩放。"""
    return 1.0

def smooth(prev, cur, alpha):
    """平滑帧时间：EMA 滤波，避免负载突变时按单帧抖动做决策。"""
    return prev + alpha * (cur - prev)

def step(cur, target, max_step):
    """小步进：每次调整不超过 max_step，避免跨台阶切档。"""
    delta = target - cur
    if delta > max_step:
        delta = max_step
    elif delta < -max_step:
        delta = -max_step
    return cur + delta

def band(value, lo, hi):
    """滞回区间：帧时间落在 [lo, hi] 内时保持当前分辨率，防止来回横跳。"""
    return lo <= value <= hi

def reproject(uv, delta):
    """历史重投影：分辨率变化后按运动矢量偏移采样历史缓冲，消除 TAA 残影。"""
    return (uv[0] + delta[0], uv[1] + delta[1])

def taa(base, scale):
    """TAA 按比例：历史缓冲/抖动幅度随渲染比例缩放。"""
    return base * scale

def bloom(base, scale):
    """后处理按比例：bloom 等后处理目标按渲染比例分配，保持光晕比例一致。"""
    return base * scale

def sharpen(strength, scale):
    """锐化补偿：低分辨率下按 1/scale 提升锐化强度，抵消上采样软化。"""
    return strength / scale

def per_cam(camera_id):
    """按相机独立：每个相机维护独立的缩放因子键。"""
    return f"res:{camera_id}"

def res(width, scale):
    """分辨率计算。"""
    return int(width * scale)

def pct(native, current):
    """比例。"""
    return current / native

def clamp_scale(scale):
    """缩放钳制：限制在 [0.5, 1.0]，避免过低分辨率不可用。"""
    return max(0.5, min(1.0, scale))

def fps(frame_ms):
    """帧率。"""
    return 1000.0 / frame_ms

def key(camera_id):
    """相机键。"""
    return f"cam:{camera_id}"
