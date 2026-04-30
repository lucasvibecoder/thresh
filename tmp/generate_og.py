"""
Generate OG social preview image for runthresh.com
1200x630px, dark terminal aesthetic
"""
from PIL import Image, ImageDraw, ImageFont
import random
import math

# --- Config ---
W, H = 1200, 630
BG = (8, 8, 8)            # #080808
GREEN = (0, 255, 65)       # #00FF41
ORANGE = (212, 98, 43)     # #D4622B
TEXT = (232, 234, 240)      # #E8EAF0
MUTED = (156, 161, 170)    # #9CA1AA
DIM = (40, 42, 46)         # very faint for scanlines/grid

FONT_DIR = "/Users/lucas/Documents/projects/thresh/tmp/fonts/jbmono/fonts/ttf"
OUT_PATH = "/Users/lucas/Documents/projects/thresh/og-image.png"

# --- Load fonts ---
font_bold_72 = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Bold.ttf", 72)
font_bold_48 = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Bold.ttf", 48)
font_reg_28 = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Regular.ttf", 28)
font_reg_22 = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Regular.ttf", 22)
font_light_18 = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Light.ttf", 18)
font_reg_16 = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Regular.ttf", 16)

# --- Create canvas ---
img = Image.new("RGB", (W, H), BG)
draw = ImageDraw.Draw(img)

# --- Subtle grid pattern ---
for x in range(0, W, 40):
    draw.line([(x, 0), (x, H)], fill=(14, 14, 14), width=1)
for y in range(0, H, 40):
    draw.line([(0, y), (W, y)], fill=(14, 14, 14), width=1)

# --- Scanlines (very subtle) ---
for y in range(0, H, 3):
    draw.line([(0, y), (W, y)], fill=(0, 0, 0, 30), width=1)

# --- Decorative background code fragments (very dim, sparse) ---
# Only a handful, placed carefully to avoid content areas
frag_data = [
    ("signal.match(buyer_intent)", 720, 40, (0, 30, 8)),
    ("if score > 0.85: route()", 920, 90, (0, 28, 7)),
    ("pipeline.filter(noise)", 900, 540, (0, 28, 7)),
    ("outbound.send(precision)", 280, 110, (18, 18, 20)),
    ("enrich(contact, firmographic)", 430, 130, (18, 18, 20)),
    ("  yield prospect.engage()", 140, 138, (18, 18, 20)),
    ("score = model.predict(fit)", 780, 100, (18, 18, 20)),
]
for frag, fx, fy, c in frag_data:
    draw.text((fx, fy), frag, font=font_reg_16, fill=c)

# --- Top-left terminal prompt ---
draw.text((48, 36), "$ thresh --deploy", font=font_reg_22, fill=(0, 120, 30))

# --- Green accent line (top) ---
draw.rectangle([(48, 72), (280, 74)], fill=GREEN)

# --- Wordmark: THRESH_ ---
wordmark = "THRESH_"
wm_x, wm_y = 48, 180
# Glow effect (draw text multiple times with slight offsets in dim green)
for offset in [3, 2, 1]:
    draw.text((wm_x - offset, wm_y), wordmark, font=font_bold_72, fill=(0, 60, 15))
    draw.text((wm_x + offset, wm_y), wordmark, font=font_bold_72, fill=(0, 60, 15))
    draw.text((wm_x, wm_y - offset), wordmark, font=font_bold_72, fill=(0, 60, 15))
    draw.text((wm_x, wm_y + offset), wordmark, font=font_bold_72, fill=(0, 60, 15))
# Main text
draw.text((wm_x, wm_y), wordmark, font=font_bold_72, fill=GREEN)

# --- Tagline ---
tagline = "Signal-based outbound for niche B2B"
draw.text((52, 280), tagline, font=font_reg_28, fill=TEXT)

# --- Subline ---
subline = "// precision prospecting, zero noise"
draw.text((52, 325), subline, font=font_reg_22, fill=MUTED)

# --- Orange accent block (visual separator) ---
draw.rectangle([(48, 380), (52, 430)], fill=ORANGE)

# --- Status lines (terminal output vibe) ---
status_lines = [
    ("[READY]  ICP signals locked", GREEN),
    ("[ACTIVE] Outbound sequences running", ORANGE),
    ("[LIVE]   Pipeline conversion: 3.2x avg", TEXT),
]
for i, (line, color) in enumerate(status_lines):
    y_pos = 388 + i * 32
    # Bracket/prefix in brighter color, rest in slightly muted
    bracket_end = line.index("]") + 1
    draw.text((72, y_pos), line[:bracket_end], font=font_reg_22, fill=color)
    draw.text((72 + draw.textlength(line[:bracket_end], font=font_reg_22), y_pos),
              line[bracket_end:], font=font_reg_22, fill=MUTED)

# --- Right side: decorative data block ---
block_x = 660
block_y = 140
block_w = 500
block_h = 350
# Faint bordered box
draw.rectangle([(block_x, block_y), (block_x + block_w, block_y + block_h)],
               outline=(30, 30, 30), width=1)
# Header bar
draw.rectangle([(block_x, block_y), (block_x + block_w, block_y + 36)],
               fill=(18, 18, 18))
draw.text((block_x + 12, block_y + 8), "signal_feed.log", font=font_reg_16, fill=MUTED)
# Dots (window controls)
for j, dc in enumerate([(60, 60, 60), (60, 60, 60), (60, 60, 60)]):
    dot_x = block_x + block_w - 60 + j * 18
    draw.ellipse([(dot_x, block_y + 11), (dot_x + 12, block_y + 23)], fill=dc)

# Log lines (use font_reg_16 for tighter fit)
font_log = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Regular.ttf", 15)
font_log_light = ImageFont.truetype(f"{FONT_DIR}/JetBrainsMono-Light.ttf", 15)
log_lines = [
    ("14:23:01", "MATCH ", "VP Sales @ Series B SaaS", GREEN),
    ("14:23:04", "ENRICH", "firmographic + tech stack", (0, 180, 50)),
    ("14:23:07", "SCORE ", "intent: 0.92 | fit: 0.88", ORANGE),
    ("14:23:09", "ROUTE ", "sequence: high-intent-demo", TEXT),
    ("14:23:12", "MATCH ", "Head of Ops @ fintech", GREEN),
    ("14:23:15", "FILTER", "noise removed: 847 signals", MUTED),
    ("14:23:18", "SCORE ", "intent: 0.79 | fit: 0.94", ORANGE),
    ("14:23:21", "SEND  ", "personalized outreach queued", GREEN),
    ("14:23:24", "MATCH ", "CRO @ vertical SaaS", GREEN),
    ("14:23:27", "ENRICH", "intent + hiring signals", (0, 180, 50)),
]
for i, (ts, tag, msg, color) in enumerate(log_lines):
    ly = block_y + 50 + i * 29
    draw.text((block_x + 12, ly), ts, font=font_log_light, fill=(60, 60, 60))
    draw.text((block_x + 105, ly), tag, font=font_log, fill=color)
    draw.text((block_x + 175, ly), msg, font=font_log_light, fill=(90, 94, 100))

# --- Bottom bar ---
draw.rectangle([(0, H - 48), (W, H)], fill=(12, 12, 12))
draw.text((48, H - 38), "runthresh.com", font=font_reg_22, fill=GREEN)
draw.text((W - 320, H - 36), "outbound infrastructure", font=font_light_18, fill=MUTED)

# --- Corner accents (square terminal feel) ---
corner_len = 20
corner_color = (0, 100, 25)
# Top-left
draw.line([(16, 16), (16 + corner_len, 16)], fill=corner_color, width=2)
draw.line([(16, 16), (16, 16 + corner_len)], fill=corner_color, width=2)
# Top-right
draw.line([(W - 16 - corner_len, 16), (W - 16, 16)], fill=corner_color, width=2)
draw.line([(W - 16, 16), (W - 16, 16 + corner_len)], fill=corner_color, width=2)
# Bottom-left (above bottom bar)
draw.line([(16, H - 64), (16 + corner_len, H - 64)], fill=corner_color, width=2)
draw.line([(16, H - 64), (16, H - 64 + corner_len)], fill=corner_color, width=2)
# Bottom-right (above bottom bar)
draw.line([(W - 16 - corner_len, H - 64), (W - 16, H - 64)], fill=corner_color, width=2)
draw.line([(W - 16, H - 64), (W - 16, H - 64 + corner_len)], fill=corner_color, width=2)

# --- Vignette (darken edges) ---
vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vdraw = ImageDraw.Draw(vignette)
# Draw gradient rectangles from edges
for i in range(80):
    alpha = int(120 * (1 - i / 80))
    # Top
    vdraw.rectangle([(0, i), (W, i + 1)], fill=(0, 0, 0, alpha))
    # Bottom
    vdraw.rectangle([(0, H - i - 1), (W, H - i)], fill=(0, 0, 0, alpha))
    # Left
    vdraw.rectangle([(i, 0), (i + 1, H)], fill=(0, 0, 0, alpha))
    # Right
    vdraw.rectangle([(W - i - 1, 0), (W - i, H)], fill=(0, 0, 0, alpha))

img = img.convert("RGBA")
img = Image.alpha_composite(img, vignette)
img = img.convert("RGB")

# --- Save ---
img.save(OUT_PATH, "PNG", optimize=True)
print(f"OG image saved: {OUT_PATH}")
print(f"Size: {img.size[0]}x{img.size[1]}")

# Verify file size
import os
size_kb = os.path.getsize(OUT_PATH) / 1024
print(f"File size: {size_kb:.0f} KB")
