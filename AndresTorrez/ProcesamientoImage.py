import cv2

def procesar_imagen():
    ruta_imagen = input("ingrese la ruta de la image: ")
    imagen = cv2.imread(ruta_imagen)

    # convertir grises
    imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # aplicar filtro de bordes 
    bordes = cv2.Canny(imagen_gris, 100, 200)

    # guardar imagen
    salida = "imagen_bordes.png"
    cv2.imwrite(salida, bordes)
    print(f"imagen procesada guardada como: {salida}")

    # mostrar imagen
    cv2.imshow("imagen original", imagen)
    cv2.imshow("bordes detectados", bordes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

procesar_imagen()