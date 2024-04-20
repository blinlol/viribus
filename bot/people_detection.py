import torch
from torchvision import models, transforms
from PIL import Image

def init_detection_model():
    model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    return model

def get_image_path(path):
  return str(path)

detection_model = init_detection_model()
image_path = get_image_path('/content/many_people.jpg')

# Функция для обнаружения объектов на изображении
def detect_objects(image_path):
    transform = transforms.Compose([transforms.ToTensor()])
    image = Image.open(image_path)
    image_tensor = transform(image).unsqueeze(0)

    with torch.no_grad():
        predictions = detection_model(image_tensor)

    return predictions

# Функция для подсчета количества людей на изображении
def count_people(image_path):
    predictions = detect_objects(image_path)
    labels = predictions[0]['labels']
    # Класс 1 соответствует человеку
    num_people = (labels == 1).sum().item()
    return num_people

# Считаем время
def count_time(num_people):
  time = num_people * 0.5 + 1
  return time

# Собираем всю инфу
def info_stolovka(image_path):
    num_people = count_people(image_path)
    time = count_time(num_people)
    print("Загруженность столовой = {}%".format(round(num_people/60*100,2)))
    print("Время ожидания = {} минут".format(round(time)))

info_stolovka(image_path)
