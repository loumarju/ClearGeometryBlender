import bpy

##Eliminar transformaciones
#Obtén los objetos seleccionados
objects = bpy.context.selected_objects

#Itera sobre los objetos seleccionados
for obj in objects:
    #Primero lanzamos una comprobación para saber si el objeto tiene curvas de animación o no
    if obj.animation_data and obj.animation_data.action:
        #Itera sobre todas las animaciones del objeto
        for fcurve in obj.animation_data.action.fcurves:
            #Elimina todos los keyframes de la animación
            fcurve.keyframe_points.clear()
    else:
        pass

#Elimina las transformaciones de la geometría
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)


##Ordenar colecciones

def create_collection_Main(name):
    # Crea una nueva colección con el nombre dado
    new_collectionMain = bpy.data.collections.new(name)

    # Añade la nueva colección a la escena
    bpy.context.scene.collection.children.link(new_collectionMain)

    return new_collectionMain


def create_collection_shader(name, parent_collection):
    # Crea una nueva colección con el nombre dado
    new_collectionShader = bpy.data.collections.new(name)

    # Añade la nueva colección a la colección principal
    parent_collection.children.link(new_collectionShader)


def create_collection_rig(name, parent_collection):
    # Crea una nueva colección con el nombre dado
    new_collectionRig = bpy.data.collections.new(name)

    # Añade la nueva colección a la colección principal
    parent_collection.children.link(new_collectionRig)


def create_collection_rigSystem(name):
    # Crea una nueva colección con el nombre dado
    new_collection_rigSystem = bpy.data.collections.new(name)
    new_collection_rigSystem.color_tag = 'COLOR_04'

    # Añade la nueva colección a la escena
    bpy.context.scene.collection.children.link(new_collection_rigSystem)


# Crea la colección principal
main_collection = create_collection_Main('CH-Girl')

# Crea las otras colecciones y las vincula a la colección principal
create_collection_shader('cha_Girl_shader', main_collection)
create_collection_rig('cha_Girl_rig', main_collection)

# Crea la colección rig_system y la vincula a la escena
create_collection_rigSystem('rig_system')

# Obtiene la colección cha_Girl_shader
shader_collection = bpy.data.collections['cha_Girl_shader']

# Itera sobre todos los objetos seleccionados
for obj in bpy.context.selected_objects:
    # Borra el objeto de todas las colecciones
    for coll in obj.users_collection:
        coll.objects.unlink(obj)
    # Añade el objeto a la colección cha_Girl_shader
    shader_collection.objects.link(obj)


##Renombrar geometría
# Itera sobre todos los objetos seleccionados
for obj in bpy.context.selected_objects:
    # Añade el prefijo y el sufijo al nombre del objeto
    obj.name = 'geo_' + obj.name + '_00_n'






