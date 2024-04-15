import json
import os
import yaml

models_path = "Resourcepack/item-models.yml"
addons_directory = "Resourcepack/contents/"

loaded_models = {}
name_remaps = {}

# The functions

def load_model(name, path):
    no_extension = name[:name.rfind(".")]
    extension = name[name.rfind("."):]
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            load_model(file_name, path + "/" + file_name)
        return
    
    if no_extension in name_remaps:
        new_name = name_remaps[no_extension]
        new_path = path[:path.rfind("/") + 1] + new_name + extension
        os.rename(path, new_path)
        # then rename any references in the file
        new_model = {}
        with open(new_path, "r") as file:
            model = json.load(file)
            model_str = json.dumps(model)
            new_model_str = model_str.replace(no_extension, new_name)
            new_model = json.loads(new_model_str)
        
        with open(new_path, "w") as file:
            json.dump(new_model, file, indent=2)
            
def load_texture(name, path):
    no_extension = name[:name.rfind(".")]
    extension = name[name.rfind("."):]
    if os.path.isdir(path):
        for file_name in os.listdir(path):
            load_texture(file_name, path + "/" + file_name)
        return
    
    if no_extension in name_remaps:
        new_name = name_remaps[no_extension]
        new_path = path[:path.rfind("/") + 1] + new_name + extension
        os.rename(path, new_path)

# Map all the models to ids
with open(models_path, "r") as models_file:
    models = yaml.safe_load(models_file)
    for item in models:
        loaded_models[models[item]] = item

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
                    new_model = old_model[:old_model.rfind("/") + 1] + mapped_name
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
        
    # Then rename and remap all model files
    for file_name in os.listdir(models):
        load_model(file_name, models + file_name)
    
    # Then rename all texture files
    for file_name in os.listdir(textures):
        load_texture(file_name, textures + file_name)