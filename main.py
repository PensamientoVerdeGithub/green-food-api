from flask import Flask, request, jsonify
from PIL import Image
import requests
from io import BytesIO
import os

app = Flask(__name__)

# Ruta para fusionar múltiples capturas con el mismo mockup
@app.route('/procesar_imagenes', methods=['POST'])
def procesar_imagenes():
    try:
        data = request.json
        mockup_url = data.get("mockup_url")
        screenshot_urls = data.get("screenshot_urls")  # Lista de URLs

        if not mockup_url or not screenshot_urls:
            return jsonify({"error": "Faltan URLs"}), 400

        # Descargar el mockup (se usa la misma imagen para todas)
        mockup = Image.open(BytesIO(requests.get(mockup_url).content))

        resultados = []

        for screenshot_url in screenshot_urls:
            try:
                # Descargar la captura de pantalla
                screenshot = Image.open(BytesIO(requests.get(screenshot_url).content))

                # Redimensionar la captura al tamaño deseado
                screenshot = screenshot.resize((mockup.width - 100, mockup.height - 200))

                # Crear una copia del mockup para cada imagen
                resultado = mockup.copy()

                # Pegar la captura sobre el mockup
                x_offset = 50  # Margen X
                y_offset = 100  # Margen Y
                resultado.paste(screenshot, (x_offset, y_offset))

                # Guardar la imagen procesada en memoria
                output = BytesIO()
                resultado.save(output, format="PNG")
                output.seek(0)

                # Guardar en el servidor temporalmente
                nombre_archivo = f"imagen_{len(resultados) + 1}.png"
                with open(nombre_archivo, "wb") as f:
                    f.write(output.getvalue())

                resultados.append({"screenshot_url": screenshot_url, "archivo": nombre_archivo})

            except Exception as e:
                resultados.append({"screenshot_url": screenshot_url, "error": str(e)})

        return jsonify({"mensaje": "Imágenes procesadas", "resultados": resultados}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
  app.run(port=5000)
