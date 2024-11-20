import matplotlib.pyplot as plt
import cv2
image_path="cartas.jpg"
imagen = cv2.imread(image_path)
imagen_gris= cv2.cvtColor(imagen, cv2.COLOR_RGB2GRAY)
bordes_canny = cv2.Canny(imagen_gris, 100, 200)

plt.imshow(bordes_canny)
ruta_salida = "bordes_canny.jpg"
cv2.imwrite(ruta_salida, bordes_canny)