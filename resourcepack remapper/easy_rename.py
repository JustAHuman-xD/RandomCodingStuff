import json
import os
import yaml

models_path = "Resourcepack/item-models.yml"
addons_directory = "Resourcepack/contents/"

valid_names = []
loaded_models = {}
name_remaps = {}

# The functions

def findRemap(name):
    if name in valid_names:
        return None
    
    weight = 0
    match = None
    for key in name_remaps:
        if key in name:
            new_weight = len(key)
            if new_weight > weight:
                weight = new_weight
                match = key
    return match

def rename_dir(name, path):
    if not os.path.isdir(path):
        return
    
    match = findRemap(name)
    if match != None:
        new_name = name.replace(match, name_remaps[match])
        new_path = path.replace(name, new_name)
        os.rename(path, new_path)
        name = new_name
        path = new_path
    
    for file_name in os.listdir(path):
        rename_dir(file_name, path + "/" + file_name)

def load_model(name, path):
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            load_model(file_name, path + "/" + file_name)
        return
    
    no_extension = name[:name.rfind(".")]
    match = findRemap(no_extension)
    if match != None:
        new_name = name.replace(match, name_remaps[match])
        new_path = path.replace(name, new_name)
        os.rename(path, new_path)
        # then rename any references in the file
        lines = []
        with open(new_path, "r") as file:
            for line in file:
                lines.append(line.replace(match, name_remaps[match]))
        
        with open(new_path, "w") as file:
            file.writelines(lines)
            
def load_texture(name, path):
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            load_texture(file_name, path + "/" + file_name)
        return
    
    no_extension = name[:name.rfind(".")]
    match = findRemap(no_extension)
    if match != None:
        new_name = name.replace(match, name_remaps[match])
        new_path = path.replace(name, new_name)
        os.rename(path, new_path)

# Map all the models to ids
with open(models_path, "r") as models_file:
    models = yaml.safe_load(models_file)
    for item in models:
        loaded_models[models[item]] = item
        valid_names.append(item)

# Go through every category
for addon_name in os.listdir(addons_directory):
    # ignore internal directory
    if addon_name == "_iainternal":
        continue
    
    addon_dir = addons_directory + addon_name + "/"
    configs = addon_dir + "configs/"
    pack = addon_dir + "resourcepack/" + addon_name + "/"
    models = pack + "models/"
    textures = pack + "textures/"
    
    # Start by remapping all configs
    for config_file in os.listdir(configs):
        config_object = None
        new_config_object = {}
        config_path = configs + config_file
        with open(config_path, "r") as config:
            config_object = yaml.safe_load(config)
            # Save any other data identically
            for other_key in config_object:
                if not other_key == "items":
                    new_config_object[other_key] = config_object[other_key]
            # Remap Item Names
            new_config_object["items"] = {}
            for item in config_object["items"]:
                item_body = config_object["items"][item]
                model_id = item_body["resource"]["model_id"]
                mapped_name = loaded_models[model_id].lower()
                if mapped_name != item and model_id in loaded_models:
                    old_model = item_body["resource"]["model_path"]
                    new_model = old_model.replace(item, mapped_name)
                    item_body["resource"]["model_path"] = new_model
                    new_config_object["items"][mapped_name] = item_body
                    name_remaps[item] = mapped_name
                else:
                    new_config_object["items"][item] = item_body
        # Save the new mappings
        with open(config_path, "w") as config:
            yaml.dump(new_config_object, config, sort_keys=False)
        # Fix the model paths not having quotes manually because fuck pyyaml
        lines = []
        with open(config_path, "r") as config:
            for line in config:
                if not "model_path:" in line:
                    lines.append(line)
                    continue
                key = line[:line.rfind(":") + 1]
                value = line[line.rfind(":") + 1:].strip()
                lines.append(key + " \"" + value + "\"\n")
        with open(config_path, "w") as config:
            config.writelines(lines)
    
    # Then rename any directories
    for file_name in os.listdir(models):
        rename_dir(file_name, models + file_name)
    
    for file_name in os.listdir(textures):
        rename_dir(file_name, textures + file_name)
    
    # Then rename and remap all model files
    for file_name in os.listdir(models):
        load_model(file_name, models + file_name)
    
    # Then rename all texture files
    for file_name in os.listdir(textures):
        load_texture(file_name, textures + file_name)