from PIL import Image
import json
import random

createComposite = False
createPixelsModels = False
createCommands = False
createPixelTextures = False
logCompositeLines = True

if createComposite:
    # Generate the composite model
    with open("resource_gen/generated/composite.json", "w") as file:
        model = {
            "model": {
                "type": "minecraft:composite",
                "models": []
            }
        }
        models = model["model"]["models"]
        for i in range(16 * 16):
            models.append({
                "type": "minecraft:model",
                "model": "minecraft:item/pixel_" + str(i),
                "tints": [{
                    "type": "minecraft:custom_model_data",
                    "index": i,
                    "default": 16777215
                }]
            })
        
        file.write(json.dumps(model, indent=4))

if createPixelsModels:
    # Generate the models for the pixels
    for i in range(16 * 16):
        with open("resource_gen/generated/pixel_" + str(i) + ".json", "w") as file:
            model = {
                "parent": "humans_world_map:item/pixel",
                "textures": {
                    "layer0": "humans_world_map:item/region/pixel_" + str(i)
                }
            }
            file.write(json.dumps(model, indent=4))

if createCommands:
    with open("resource_gen/generated/commands.json", "w") as file:
        commands = {}
        give_command = "/give @s minecraft:iron_ingot[item_model=\"minecraft:gui_map\",custom_model_data={colors:["
        for i in range(16 * 16):
            if i > 0:
                give_command += ","
            # pack random rgb to a single integer
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = (r << 16) + (g << 8) + b
            give_command += str(color)
        give_command += "]}]"
        commands["give_command"] = give_command
        file.write(json.dumps(commands, indent=4))

if createPixelTextures:
    for i in range(256):
        with open("resource_gen/textures/pixel_" + str(i) + ".png", "wb") as file:
            img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
            pixels = img.load()
            row = i // 16
            col = i % 16
            pixels[col, row] = (255, 255, 255, 255)
            img.save(file)

if logCompositeLines:
    for i in range(16 * 16):
        print("{\"type\":\"minecraft:model\",\"model\":\"humans_world_map:item/region/pixel_" + str(i) + "\",\"tints\":[{\"type\":\"minecraft:custom_model_data\",\"default\":16777215,\"index\":" + str(i) + "}]},")