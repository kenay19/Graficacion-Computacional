import numpy as np
import matplotlib.pyplot as plt

w = 400
h = 300

# Normaliza vectores
def normalize(x):
    x /= np.linalg.norm(x)
    return x

# Intersecta el plano
def intersect_plane(O, D, P, N):
    # Devuelve la distancia de O a la intersección del rayo (O, D)
    # con el plano (P, N), o +inf si no hay intersección.
    # O y P son puntos 3D, D y N (normales) son vectores normalizados.
    denom = np.dot(D, N)
    if np.abs(denom) < 1e-6:
        return np.inf
    d = np.dot(P - O, N) / denom
    if d < 0:
        return np.inf
    return d

# Interseccion en la esfera
def intersect_sphere(O, D, S, R):
    # Devuelve la distancia de O a la intersección del rayo (O, D)
    # con la esfera (S, R), o +inf si no hay intersección.
    # O y S son puntos 3D, D (dirección) es un vector normalizado, R es un escalar.
    a = np.dot(D, D)
    OS = O - S
    b = 2 * np.dot(D, OS)
    c = np.dot(OS, OS) - R * R
    disc = b * b - 4 * a * c
    if disc > 0:
        distSqrt = np.sqrt(disc)
        q = (-b - distSqrt) / 2.0 if b < 0 else (-b + distSqrt) / 2.0
        t0 = q / a
        t1 = c / q
        t0, t1 = min(t0, t1), max(t0, t1)
        if t1 >= 0:
            return t1 if t0 < 0 else t0
    return np.inf

# Intersecciones
def intersect(O, D, obj):
    if obj['type'] == 'plane':
        return intersect_plane(O, D, obj['position'], obj['normal'])
    elif obj['type'] == 'sphere':
        return intersect_sphere(O, D, obj['position'], obj['radius'])


def get_normal(obj, M):
    # Encuentra el vector normal.
    if obj['type'] == 'sphere':
        N = normalize(M - obj['position'])
    elif obj['type'] == 'plane':
        N = obj['normal']
    return N

# Obtiene el color
def get_color(obj, M):
    color = obj['color']
    if not hasattr(color, '__len__'):
        color = color(M)
    return color


def trace_ray(rayO, rayD):
    # Encuentra el primer punto de intersección con la escena.
    t = np.inf
    for i, obj in enumerate(scene):
        t_obj = intersect(rayO, rayD, obj)
        if t_obj < t:
            t, obj_idx = t_obj, i
    # Devuelve none si el rayo no intersecta ningún objeto.
    if t == np.inf:
        return
    # Encuentra el objeto
    obj = scene[obj_idx]
    # Encuentre el punto de intersección en el objeto.
    M = rayO + rayD * t
    # Encuentra las propiedades del objeto.
    N = get_normal(obj, M)
    color = get_color(obj, M)
    toL = normalize(L - M)
    toO = normalize(O - M)
    # Shadow: Encontrar si el punto está sombreado o no.
    l = [intersect(M + N * .0001, toL, obj_sh)
         for k, obj_sh in enumerate(scene) if k != obj_idx]
    if l and min(l) < np.inf:
        return
    # Comience a calcular el color.
    col_ray = ambient
    # Sombreado Lambert (difuso).
    col_ray += obj.get('diffuse_c', diffuse_c) * max(np.dot(N, toL), 0) * color
    # Blinn-Phong shading (specular).
    col_ray += obj.get('specular_c', specular_c) * max(np.dot(N, normalize(toL + toO)), 0) ** specular_k * color_light
    return obj, M, N, col_ray

# Añade las esferas
def add_sphere(position, radius, color):
    return dict(type='sphere', position=np.array(position),
                radius=np.array(radius), color=np.array(color), reflection=.5)

# Añade el plano
def add_plane(position, normal):
    return dict(type='plane', position=np.array(position),
                normal=np.array(normal),
                color=lambda M: (color_plane0
                                 if (int(M[0] * 2) % 2) == (int(M[2] * 2) % 2) else color_plane1),
                diffuse_c=.75, specular_c=.5, reflection=.25)


# Lista de esferas.
color_plane0 = 1. * np.ones(3)
color_plane1 = 0. * np.ones(3)
scene = [add_sphere([.75, .1, 1.], .6, [0., 0., 1.]),
         add_sphere([-.75, .1, 2.25], .6, [.5, .223, .5]),
         add_sphere([-2.75, .1, 3.5], .6, [1., .572, .184]),
         add_plane([0., -.5, 0.], [0., 1., 0.]),
         ]

# Posición y color de la luz.
L = np.array([5., 5., -10.])
color_light = np.ones(3)

# Parámetros predeterminados de luz y material.
ambient = .05
diffuse_c = 1.
specular_c = 1.
specular_k = 50

depth_max = 5  # Número máximo de reflejos de luz.
col = np.zeros(3)  # color actual.
O = np.array([0., 0.35, -1.])  # Camera.
Q = np.array([0., 0., 0.])  # Camara apuntadondo
img = np.zeros((h, w, 3))

r = float(w) / h
# Coordenadas de pantalla: x0, y0, x1, y1.
S = (-1., -1. / r + .25, 1., 1. / r + .25)

# Bucle a través de todos los píxeles.
for i, x in enumerate(np.linspace(S[0], S[2], w)):
    if i % 10 == 0:
        print(i / float(w) * 100, "%")
    for j, y in enumerate(np.linspace(S[1], S[3], h)):
        col[:] = 0
        Q[:2] = (x, y)
        D = normalize(Q - O)
        depth = 0
        rayO, rayD = O, D
        reflection = 1.
        # Bucle a través de los rayos inicial y secundario.
        while depth < depth_max:
            traced = trace_ray(rayO, rayD)
            if not traced:
                break
            obj, M, N, col_ray = traced
            # Reflexión: crear un nuevo rayo.
            rayO, rayD = M + N * .0001, normalize(rayD - 2 * np.dot(rayD, N) * N)
            depth += 1
            col += reflection * col_ray
            reflection *= obj.get('reflection', 1.)
        img[h - j - 1, i, :] = np.clip(col, 0, 1)

plt.imsave('fig.png', img)