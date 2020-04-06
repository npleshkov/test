from PIL import Image, ImageEnhance
def add_watermark(image, watermark, opacity=1, wm_interval=0):
    assert opacity >= 0 and opacity <= 1
    if opacity < 1:
        if watermark.mode != 'RGBA':
            watermark = watermark.convert('RGBA')
        else:
            watermark = watermark.copy()
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)
    layer = Image.new('RGBA', image.size, (0,0,0,0))
    for y in range(0, image.size[1], watermark.size[1]+wm_interval):
        for x in range(0, image.size[0], watermark.size[0]+wm_interval):
            layer.paste(watermark, (x, y))
    return Image.composite(layer,  image,  layer)

# image - картинка, на которую накладываете изображение
# watermark - картинка, которую накладываете
# opacity - прозрачность
# wm_interval - интервал между изображениями watermark
# !!! watermark накладывается рекурсивно по всему полю изображения. Функция возвращает уже готовое изображение, которое надо еще сохранить.
#
# !!! если что-то не получается, сперва проверьте, может ли ваш PIL обрабатывать изображения jpeg, png, gif. бывает что PIL установлен, но всем любимые форматы вовсе не поддерживает, т.к. не (корректно) установлен libjpeg и т.п.
#
