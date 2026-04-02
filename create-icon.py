from PIL import Image, ImageDraw

# Create a 512x512 icon that resembles the LockDown Browser icon
size = 512
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

cx, cy = size // 2, size // 2
s = 2  # scale factor from 256

# Diamond shape (rotated square) - yellow/gold
diamond_points = [
    (cx, cy - 90*s),
    (cx + 90*s, cy),
    (cx, cy + 90*s),
    (cx - 90*s, cy),
]
outer_diamond = [
    (cx, cy - 95*s),
    (cx + 95*s, cy),
    (cx, cy + 95*s),
    (cx - 95*s, cy),
]
draw.polygon(outer_diamond, fill=(180, 140, 20, 255))
draw.polygon(diamond_points, fill=(230, 190, 40, 255))

# Highlight
highlight_points = [
    (cx, cy - 85*s),
    (cx + 50*s, cy - 35*s),
    (cx, cy + 15*s),
    (cx - 50*s, cy - 35*s),
]
draw.polygon(highlight_points, fill=(250, 215, 80, 180))

# Padlock body
lock_w, lock_h = 44*s, 36*s
lock_x = cx - lock_w // 2
lock_y = cy - 6*s
draw.rounded_rectangle(
    [lock_x, lock_y, lock_x + lock_w, lock_y + lock_h],
    radius=8,
    fill=(50, 50, 55, 255)
)

# Shackle
shackle_w = 28*s
shackle_x = cx - shackle_w // 2
shackle_y = lock_y - 22*s
draw.arc(
    [shackle_x, shackle_y, shackle_x + shackle_w, shackle_y + shackle_w],
    180, 0, fill=(50, 50, 55, 255), width=12
)
draw.rectangle([shackle_x, shackle_y + shackle_w // 2, shackle_x + 12, lock_y + 4], fill=(50, 50, 55, 255))
draw.rectangle([shackle_x + shackle_w - 12, shackle_y + shackle_w // 2, shackle_x + shackle_w, lock_y + 4], fill=(50, 50, 55, 255))

# Keyhole
keyhole_cx = cx
keyhole_cy = lock_y + 14*s
draw.ellipse([keyhole_cx - 10, keyhole_cy - 10, keyhole_cx + 10, keyhole_cy + 10], fill=(20, 20, 20, 255))
draw.polygon([
    (keyhole_cx - 6, keyhole_cy + 6),
    (keyhole_cx + 6, keyhole_cy + 6),
    (keyhole_cx + 2, keyhole_cy + 28),
    (keyhole_cx - 2, keyhole_cy + 28),
], fill=(20, 20, 20, 255))

# Colored squares at bottom-right
sq_size = 16*s
sq_x = cx + 18*s
sq_y = cy + 40*s
draw.rectangle([sq_x, sq_y, sq_x + sq_size, sq_y + sq_size], fill=(40, 100, 200, 255))
draw.rectangle([sq_x + sq_size + 4, sq_y, sq_x + sq_size * 2 + 4, sq_y + sq_size], fill=(230, 190, 40, 255))
draw.rectangle([sq_x + sq_size + 4, sq_y - sq_size - 4, sq_x + sq_size * 2 + 4, sq_y - 4], fill=(40, 100, 200, 255))
draw.rectangle([sq_x, sq_y - sq_size - 4, sq_x + sq_size, sq_y - 4], fill=(60, 180, 60, 255))

# Save PNG
img.save('icon.png', 'PNG')

# Save ICO with proper 256x256 embedded
ico_img = img.resize((256, 256), Image.LANCZOS)
ico_img.save('icon.ico', format='ICO', sizes=[(256, 256)])

print("Created icon.png (512x512) and icon.ico (256x256)")
