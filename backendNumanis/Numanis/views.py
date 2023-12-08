import os
import uuid

import requests
from ninja import Router
import pillow_avif
from PIL import Image
from django.http import JsonResponse, FileResponse, HttpResponse
from io import BytesIO

router = Router()


@router.get("/hello")
def hello(request):
    return {"message": "Hello, Ninja API!"}


@router.post("/imagel")
def compressImageLocale(request):
    # Assurez-vous que le champ 'image' correspond à l'attribut 'name' de votre champ de fichier dans le formulaire HTML
    uploaded_file = request.FILES.get('image', None)

    if uploaded_file:

        # Maintenant, vous pouvez ouvrir et compresser l'image
        image = Image.open(uploaded_file)

        if image.mode != 'RGB':
            image = image.convert('RGB')

        # Sauvegarder l'image compressée (remplacez 'image-file-compressed' par le chemin de destination souhaité)

        output_buffer = BytesIO()

        image.save(output_buffer, format='AVIF', quality=1)  # Ajustez la qualité selon vos besoins

        # Retourner l'image compressée comme réponse HTTP
        response = HttpResponse(output_buffer.getvalue(), content_type='image/avif')
        response[
            'Content-Disposition'] = 'inline; filename=image-file-compressed.avif'  # Pour afficher l'image dans le navigateur

        return response

    else:
        return JsonResponse({"message": "Aucun fichier n'a été envoyé"}, status=400)


@router.get("/image")
def compressImageWIthURL(request, url: str = None, target_size_kb: int = 100):
    if url:
        # Télécharger l'image depuis l'URL
        try:
            image_response = requests.get(url, stream=True)
            image_response.raise_for_status()

            # Ouvrir et compresser l'image téléchargée
            image = Image.open(BytesIO(image_response.content))

            # Obtenez les dimensions de l'image d'entrée
            input_dimensions = image.size
            input_format = image.format
            input_size = len(image_response.content)

            if image.mode != 'RGB':
                image = image.convert('RGB')

            # Sauvegarder l'image compressée dans un répertoire défini (par exemple, 'media/compressed_images/')
            compressed_directory = "media/compressed_images/"

            # Vérifier si le répertoire existe
            if not os.path.exists(compressed_directory):
                # Si le répertoire n'existe pas, le créer
                os.makedirs(compressed_directory)

            compressed_filename = f"{uuid.uuid4().hex}.avif"
            compressed_filepath = os.path.join("media/compressed_images/", compressed_filename)

            image.save(compressed_filepath, format='AVIF',
                       quality=target_size_kb)  # Ajustez la qualité selon vos besoins

            # Obtenez les dimensions de l'image compressée
            output_dimensions = image.size
            output_format = 'AVIF'  # Le format de sortie est toujours AVIF dans cet exemple
            output_size = os.path.getsize(compressed_filepath)

            # Retourner l'URL relative de l'image compressée
            compressed_url = f"/media/compressed_images/{compressed_filename}"
            # Construire l'URL absolue en utilisant request.build_absolute_uri
            compressed_url_absolute = request.build_absolute_uri(compressed_url)

            return JsonResponse({"compressed_url": compressed_url_absolute,
                                 "input_size": input_size,
                                 "output_size": output_size,
                                 "input_dimensions": input_dimensions,
                                 "output_dimensions": output_dimensions,
                                 "input_format": input_format,
                                 "output_format": output_format,
                                 })

        except requests.RequestException as e:
            return JsonResponse({"message": f"Erreur lors du téléchargement de l'image depuis l'URL : {str(e)}"},
                                status=500)

    else:
        return JsonResponse({"message": "Aucune URL d'image n'a été fournie"}, status=400)


@router.get("/video")
def hello(request):
    return {"message": "Hello, Ninja API!"}
