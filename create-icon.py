from PIL import Image, ImageDraw

# Create a 256x256 icon matching the real LockDown Browser icon
# Key: small, compact, lots of whitespace, silver padlock, tiny Windows flag
size = 256
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

cx, cy = size // 2, size // 2

# ---- Small diamond (rotated square) ~35% of canvas ----
r = 48  # diamond radius (half-diagonal)

# Outer diamond border - darker gold
outer_r = r + 3
outer_diamond = [
    (cx, cy - outer_r),
    (cx + outer_r, cy),
    (cx, cy + outer_r),
    (cx - outer_r, cy),
]
draw.polygon(outer_diamond, fill=(185, 145, 25, 255))

# Main diamond - golden yellow
diamond = [
    (cx, cy - r),
    (cx + r, cy),
    (cx, cy + r),
    (cx - r, cy),
]
draw.polygon(diamond, fill=(225, 185, 40, 255))

# Highlight on upper portion
highlight = [
    (cx, cy - r + 4),
    (cx + r * 0.55, cy - r * 0.25),
    (cx, cy + r * 0.15),
    (cx - r * 0.55, cy - r * 0.25),
]
draw.polygon(highlight, fill=(245, 215, 75, 160))

# ---- Silver/gray padlock ----
# Lock body
lock_w, lock_h = 22, 18
lock_x = cx - lock_w // 2
lock_y = cy - 2
draw.rounded_rectangle(
    [lock_x, lock_y, lock_x + lock_w, lock_y + lock_h],
    radius=3,
    fill=(120, 120, 130, 255)
)
# Lock body highlight
draw.rounded_rectangle(
    [lock_x + 2, lock_y + 1, lock_x + lock_w - 2, lock_y + lock_h - 2],
    radius=2,
    fill=(155, 155, 165, 255)
)

# Shackle (U-shape above lock body)
shackle_w = 14
shackle_x = cx - shackle_w // 2
shackle_y = lock_y - 12
# Outer shackle arc
draw.arc(
    [shackle_x, shackle_y, shackle_x + shackle_w, shackle_y + shackle_w],
    180, 0, fill=(100, 100, 110, 255), width=4
)
# Left bar
draw.rectangle([shackle_x, shackle_y + shackle_w // 2, shackle_x + 3, lock_y + 1],
               fill=(100, 100, 110, 255))
# Right bar
draw.rectangle([shackle_x + shackle_w - 3, shackle_y + shackle_w // 2, shackle_x + shackle_w, lock_y + 1],
               fill=(100, 100, 110, 255))
# Shackle highlight (inner lighter arc)
draw.arc(
    [shackle_x + 2, shackle_y + 2, shackle_x + shackle_w - 2, shackle_y + shackle_w - 2],
    180, 0, fill=(170, 170, 180, 255), width=2
)

# Keyhole
kh_cx, kh_cy = cx, lock_y + 8
draw.ellipse([kh_cx - 3, kh_cy - 3, kh_cx + 3, kh_cy + 3], fill=(70, 70, 75, 255))
draw.polygon([
    (kh_cx - 1.5, kh_cy + 2),
    (kh_cx + 1.5, kh_cy + 2),
    (kh_cx + 0.5, kh_cy + 8),
    (kh_cx - 0.5, kh_cy + 8),
], fill=(70, 70, 75, 255))

# ---- Tiny Windows-flag colored squares at bottom-right of diamond ----
sq = 7  # square size
gap = 1
flag_x = cx + 12  # offset right of center
flag_y = cy + 20  # offset below center

# 2x2 grid: red, green / blue, yellow (Windows flag colors)
draw.rectangle([flag_x, flag_y, flag_x + sq, flag_y + sq],
               fill=(243, 83, 37, 255))       # red (top-left)
draw.rectangle([flag_x + sq + gap, flag_y, flag_x + sq * 2 + gap, flag_y + sq],
               fill=(129, 188, 6, 255))        # green (top-right)
draw.rectangle([flag_x, flag_y + sq + gap, flag_x + sq, flag_y + sq * 2 + gap],
               fill=(5, 166, 240, 255))        # blue (bottom-left)
draw.rectangle([flag_x + sq + gap, flag_y + sq + gap, flag_x + sq * 2 + gap, flag_y + sq * 2 + gap],
               fill=(255, 186, 8, 255))        # yellow (bottom-right)

# Save PNG
img.save('icon.png', 'PNG')

# Save ICO - embed at 256x256
img.save('icon.ico', format='ICO', sizes=[(256, 256)])

print("Created icon.png and icon.ico (256x256)")
