from rest_framework import serializers, viewsets
from .models import DetectionResult
from django.shortcuts import render
import tensorflow as tf
from django.utils.decorators import method_decorator
from django.conf import settings
from django.views import View
from .formulaire import DetectionResultForm
from django.views.decorators.csrf import csrf_exempt
import shutil
import numpy as np
import os
from django.http import JsonResponse

class DetectionResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetectionResult
        fields = '__all__'

class DetectionResultViewSet(viewsets.ModelViewSet):
    queryset = DetectionResult.objects.all()
    serializer_class = DetectionResultSerializer





@method_decorator(csrf_exempt, name='dispatch')
class PredictMaladie(View):

    def get(self, request):
        form = DetectionResultForm()
        return render(request, 'upload_form.html', {'form': form})

    def post(self, request):
        form = DetectionResultForm(request.POST, request.FILES)
        if form.is_valid():

            detection_result = form.save(commit=False)
            detection_result.save()

        if 'image' in request.FILES:
            uploaded_image = request.FILES['image']
            destination_path = os.path.join(settings.MEDIA_ROOT, 'photos')
            os.makedirs(destination_path, exist_ok=True)
            destination_file_path = os.path.join(destination_path, 'uploaded_image.jpg')

            with open(destination_file_path, 'wb') as destination_file:
                shutil.copyfileobj(uploaded_image.file, destination_file)
            age = None  

            try:
                model_path = "C:\\Users\\jaafe\\detection_image\\projet_federateur\\ml\\V1\\models\\modelcancerlung.h5"
                model = tf.keras.models.load_model(model_path)
            except Exception as e:
                return render(request, 'error.html', {'error_message': f'Error loading the model: {str(e)}'})

            try:
                img = tf.keras.preprocessing.image.load_img(destination_file_path, target_size=(224, 224))
                img_array = tf.keras.preprocessing.image.img_to_array(img)
                img_array = tf.expand_dims(img_array, 0)
                img_array /= 255.0

                predictions = model.predict(img_array)
                predictions_list = predictions.tolist()

                classes = ["AdenocarcinomaChest Lung Cancer", "Large cell carcinoma Lung Cancer", "NORMAL lung", "Squamous cell carcinoma Lung Cancer"]
                predicted_class_index = np.argmax(predictions_list)
                predicted_class = classes[predicted_class_index]

                result = {
                    'image': destination_file_path,
                    'maladie': predicted_class,
                    
                }

                return render(request, 'result.html', {'results': [result]})

          
            except Exception as e:
                return JsonResponse({'error': f'Error making predictions: {str(e)}'}, status=500)

        else:
            return JsonResponse({'error': 'Missing "image" field in the request'}, status=400)



