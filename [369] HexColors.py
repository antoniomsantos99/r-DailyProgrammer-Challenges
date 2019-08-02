def HexConvert(red,green,blue):
    return '#'+ hex(red)[2::].upper() +hex(green)[2::].upper() + hex(blue)[2::].upper()

print(HexConvert(255,99,71))