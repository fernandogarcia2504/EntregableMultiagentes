from .model import Ciudad, CalleSur, CalleEste, CalleNorte, CalleOeste, Edificio, Estacionamiento, Banqueta  # noqa

import mesa


def vista_general(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "rect",
        "Filled": "true",
        "Layer": 0,
        "w": 0.5,
        "h": 0.5,
        "Color": "Blue",
    }

    if (isinstance(agent, CalleSur) or isinstance(agent, CalleEste) or isinstance(agent, CalleOeste)
            or isinstance(agent, CalleNorte)):
        portrayal["Color"] = "LightGrey"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Edificio):
        portrayal["Color"] = "SkyBlue"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Estacionamiento):
        portrayal["Color"] = "Yellow"
        portrayal["w"] = 1
        portrayal["h"] = 1

    elif isinstance(agent, Estacionamiento):
        portrayal["Color"] = "Orange"
        portrayal["w"] = 0.3
        portrayal["h"] = 0.3

    elif isinstance(agent, Banqueta):
        portrayal["Color"] = "Black"
        portrayal["w"] = 1
        portrayal["h"] = 1

    # elif isinstance(agent, peaton):
    #     portrayal["Color"] = "Green"
    #     portrayal["Layer"] = 2
    #     portrayal["Shape"] = "circle"
    #     portrayal["r"] = 0.3

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    vista_general, 31, 32, 710, 710
)

model_kwargs = {"num_agents": 20, "width": 31, "height": 32}

server = mesa.visualization.ModularServer(
    Ciudad,
    [canvas_element],
    "trafico",
    model_kwargs,
)