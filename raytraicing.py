import numpy as np
import matplotlib.pyplot as plt
import imageio as io
import os
import random as ra

# Normalizar vector
def normalize(vector):
    return vector / np.linalg.norm(vector)
# Rayo reflejado
def reflected(vector, axis):
    return vector - 2 * np.dot(vector, axis) * axis
# intersección de la esfera
def sphere_intersect(center, radius, ray_origin, ray_direction):
    # Calculamos el discriminante
    b = 2 * np.dot(ray_direction, ray_origin - center)
    c = np.linalg.norm(ray_origin - center) ** 2 - radius ** 2
    delta = b ** 2 - 4 * c
    if delta > 0:  # Cuando el rayo esta apuntando directo al objeto
        # Detectar intersecciones entre un rayo y una esfera
        t1 = (-b + np.sqrt(delta)) / 2  # intersección más cercana (positiva)
        t2 = (-b - np.sqrt(delta)) / 2
        if t1 > 0 and t2 > 0:
            return min(t1, t2) # Retorna la distancia del origen del rayo hasta el punto de interseccion.
    return None  # En caso de no intersectar con ningún objeto

# objeto intersectado más cercano
def nearest_intersected_object(objects, ray_origin, ray_direction):
    #La función (sphere_intersect) encuentra el objeto más cercano que intersecta un rayo, si existe
    distances = [sphere_intersect(obj['center'], obj['radius'], ray_origin, ray_direction) for obj in objects]
    nearest_object = None #No hay ningún objeto intersectado
    min_distance = np.inf # La distancia desde el origen del rayo hasta el punto de intersección
    for index, distance in enumerate(distances):
        if distance and distance < min_distance:
            min_distance = distance
            nearest_object = objects[index]
    return nearest_object, min_distance  #((nearest objecto)->Valor es el más cercano intersectado objeto)
                                        #(min_distance) -> Distancia desde el origen hasta el punto de interseccion

#------------------------------------------------------------------------------------------------------------------------------
fotos = []
iluminaciones = [-.4,-.3,-.2,-.1,0,.1,.2,.3,.4]
posicion = [[0,0,0],[1,1,1],[2,2,2],[3,3,3],[4,4,4],[5,5,5],[5,4,3],[2,1,0],[1,4,2]]

for a in range(len(iluminaciones)):
    width = 500
    height = 500

    max_depth = 3

    camera = np.array([0, 0, 1]) #camara y pantalla. Pero la pantalla se ubica en las coordenadas x,y
    ratio = float(width) / height #tamaño deseado
    #Definimos la pantalla
    # x: -1 a 1   y: 1/ratio a -1/ratio  //esto se hace para que  la pantalla tenga la misma relación de aspecto que la imagen real
    screen = (-1, 1 / ratio, 1, -1 / ratio) #Izquierda, arriba, derecha, abajo

    # Definimos la luz de nuestra imagen que es un vector con caracteristicas
    # Definimos las mismas propiedades del modelo de reflexión de Blinn-Phong
    light = { 'position': np.array(posicion[a]), 'ambient': np.array([1, 1, 1]), 'diffuse': np.array([1, 1, 1]), 'specular': np.array([1, 1, 1]) }

    # Declaramos las esferas
    # Modelo de reflexión de Blinn-Phong
    # Color ambiente
    # Color difuso
    # Color especular
    # Brillo

    objects = [
        { 'center': np.array([-0.2, 0, -1]), 'radius': 0.3, 'ambient': np.array([0.1, 0, 0]), 'diffuse': np.array([0.7, 0, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
        { 'center': np.array([0.300, -0.3, 0]), 'radius':0.3, 'ambient': np.array([0.1, 0, 0.1]), 'diffuse': np.array([0.7, 0, 0.7]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
        { 'center': np.array([-0.3, 0, 0]), 'radius': 0.3, 'ambient': np.array([0, 0.1, 0]), 'diffuse': np.array([0, 0.6, 0]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 },
        { 'center': np.array([0, -9000, 0]), 'radius': 0.3, 'ambient': np.array([0.1, 0.1, 0.1]), 'diffuse': np.array([0.6, 0.6, 0.6]), 'specular': np.array([1, 1, 1]), 'shininess': 100, 'reflection': 0.5 }
    ]
    #Creamos la imagen
    image = np.zeros((height, width, 3))
    #Asignamos color negro a cada punto
    for i, y in enumerate(np.linspace(screen[1], screen[3], height)):
        for j, x in enumerate(np.linspace(screen[0], screen[2], width)):
            #Z es cero por que se encuentra en la pantalla
            pixel = np.array([x, y, 0])
            # La pantalla es el origen
            origin = camera
            #dirección dado el origen que es la pantalla
            direction = normalize(pixel - origin) #Normalizamos el vector
            #origen y dirección definen un rayo (linea)
            color = np.zeros((3))
            reflection = 1

            for k in range(max_depth):
                # busca intersecciones
                nearest_object, min_distance = nearest_intersected_object(objects, origin, direction)
                if nearest_object is None:
                    break # Si no hay intersecciones solo termina el programa

                #calcular el punto de intersección entre el rayo y el objeto más cercano
                intersection = origin + min_distance * direction
                normal_to_surface = normalize(intersection - nearest_object['center'])
                shifted_point = intersection + 1e-5 * normal_to_surface
                # Verificar si un objeto está sombreando el punto de intersección
                intersection_to_light = normalize(light['position'] - shifted_point)
                _, min_distance = nearest_intersected_object(objects, shifted_point, intersection_to_light)
                intersection_to_light_distance = np.linalg.norm(light['position'] - intersection)
                # Ver si el objeto más cercano devuelto está realmente más cerca que la luz del punto de intersección
                is_shadowed = min_distance < intersection_to_light_distance

                # Si usamos el punto de intersección como el origen del nuevo rayo, podríamos terminar detectando la esfera donde nos encontramos
                if is_shadowed:
                    break
                # RGB
                illumination = np.zeros((3))

                # Ambiente
                illumination += nearest_object['ambient'] * light['ambient'] + iluminaciones[a]

                # Diffuso
                illumination += nearest_object['diffuse'] * light['diffuse'] * np.dot(intersection_to_light, normal_to_surface)

                # Specular
                intersection_to_camera = normalize(camera - intersection)
                H = normalize(intersection_to_light + intersection_to_camera)
                illumination += nearest_object['specular'] * light['specular'] * np.dot(normal_to_surface, H) ** (nearest_object['shininess'] / 4)

                # Reflection
                color += reflection * illumination
                reflection *= nearest_object['reflection']

                origin = shifted_point
                direction = reflected(direction, normal_to_surface)

            image[i, j] = np.clip(color, 0, 1)

        print("%d/%d" % (i + 1, height))

    plt.imsave('image.png', image)
    fotos.append(image)
io.mimwrite('RayTracing.gif', fotos, 'GIF', duration=1)