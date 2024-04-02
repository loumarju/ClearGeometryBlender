import bpy

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

###################################################################################
#Renombrar geometría
#bpy.data.window_managers["WinMan"].(null) = 'PREFIX'
#bpy.data.window_managers["WinMan"].(null) = "geo_"
#bpy.data.window_managers["WinMan"].(null) = 'SUFFIX'
#bpy.data.window_managers["WinMan"].(null) = "_00_n"


###################################################################################
#Ordenar colecciones



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
main_collection = create_collection_Main('NombrePersonaje o Prop')

# Crea las otras colecciones y las vincula a la colección principal
create_collection_shader('NombreCarpetaShader', main_collection)
create_collection_rig('NombreCarpetaRig', main_collection)

# Crea la colección rig_system y la vincula a la escena
create_collection_rigSystem('rig_system')