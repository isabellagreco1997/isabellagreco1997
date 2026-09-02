"""Profile header in the Undertale menu style: save-file box + battle box with FIGHT/ACT/ITEM/MERCY.
python assets/make_undertale_header.py  → assets/undertale-header.png"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1600, 560
BLACK, WHITE, GREY = (0, 0, 0), (255, 255, 255), (150, 150, 150)
ORANGE, YELLOW, RED, HPRED = (255, 128, 40), (255, 255, 0), (255, 0, 0), (190, 0, 0)


def font(size, bold=True):
    for path, idx in (("/System/Library/Fonts/Menlo.ttc", 1 if bold else 0),
                      ("/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 0)):
        try:
            return ImageFont.truetype(path, size, index=idx)
        except OSError:
            continue
    return ImageFont.load_default()


def heart(d, x, y, k=4, colour=RED):
    rows = ["0110110", "1111111", "1111111", "0111110", "0011100", "0001000"]
    for j, r in enumerate(rows):
        for i, ch in enumerate(r):
            if ch == "1":
                d.rectangle([x + i * k, y + j * k, x + i * k + k - 1, y + j * k + k - 1], fill=colour)


im = Image.new("RGB", (W, H), BLACK)
d = ImageDraw.Draw(im)
F32, F28, F24 = font(32), font(28), font(24)

# ---- save file box (top left)
bx, by, bw, bh = 60, 50, 700, 210
d.rectangle([bx, by, bx + bw, by + bh], outline=WHITE, width=5)
d.text((bx + 34, by + 30), "isa", font=F32, fill=WHITE)
d.text((bx + 300, by + 30), "LV 1", font=F32, fill=WHITE)
d.text((bx + 500, by + 30), "13:37", font=F32, fill=WHITE)
d.text((bx + 34, by + 84), "london", font=F28, fill=WHITE)
heart(d, bx + 40, by + 146)
d.text((bx + 90, by + 136), "Continue", font=F28, fill=YELLOW)
d.text((bx + 340, by + 136), "Reset", font=F28, fill=WHITE)

# ---- dialogue box (top right)
tx, ty, tw, th = 820, 50, 720, 210
d.rectangle([tx, ty, tx + tw, ty + th], outline=WHITE, width=5)
lines = ["* isa appears.", "* software developer. games,", "  ai, creative tech.", "* she has too many tabs open."]
for i, l in enumerate(lines):
    d.text((tx + 34, ty + 28 + i * 40), l, font=F28, fill=WHITE)

# ---- battle strip: name / LV / HP bar
sy = 320
d.text((60, sy), "ISA", font=F28, fill=WHITE)
d.text((200, sy), "LV 1", font=F28, fill=WHITE)
d.text((360, sy + 4), "HP", font=font(20), fill=WHITE)
d.rectangle([410, sy + 2, 610, sy + 32], fill=HPRED)
d.rectangle([410, sy + 2, 610, sy + 32], fill=YELLOW)          # full
d.text((630, sy), "20 / 20", font=F28, fill=WHITE)
d.text((900, sy), "* code × imagination × intelligence", font=font(24, False), fill=GREY)

# ---- FIGHT ACT ITEM MERCY buttons
labels = ["FIGHT", "ACT", "ITEM", "MERCY"]
bwid, bhgt, gap, y0 = 300, 90, 60, 400
x = 60
for i, lab in enumerate(labels):
    sel = lab == "ACT"
    col = YELLOW if sel else ORANGE
    d.rectangle([x, y0, x + bwid, y0 + bhgt], outline=col, width=5)
    # icon
    ix, iy = x + 30, y0 + 24
    if sel:
        heart(d, ix + 4, iy + 8, k=5)            # the soul sits where the icon was, like in the game
    elif lab == "FIGHT":
        d.line([(ix, iy + 38), (ix + 34, iy + 4)], fill=col, width=6); d.line([(ix + 4, iy + 6), (ix + 14, iy + 16)], fill=col, width=6)
    elif lab == "ACT":
        d.ellipse([ix, iy + 2, ix + 36, iy + 38], outline=col, width=5); d.rectangle([ix + 14, iy + 14, ix + 22, iy + 26], fill=col)
    elif lab == "ITEM":
        d.rectangle([ix + 2, iy + 8, ix + 34, iy + 38], outline=col, width=5); d.rectangle([ix + 12, iy + 2, ix + 24, iy + 10], fill=col)
    else:
        d.rectangle([ix + 4, iy + 2, ix + 32, iy + 38], outline=col, width=5); d.line([(ix + 10, iy + 12), (ix + 26, iy + 28)], fill=col, width=5); d.line([(ix + 26, iy + 12), (ix + 10, iy + 28)], fill=col, width=5)
    d.text((x + 100, y0 + 26), lab, font=F32, fill=col)
    x += bwid + gap

im.save(os.path.join(HERE, "undertale-header.png"), optimize=True)
print("saved", im.size)
