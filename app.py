from smolagents import CodeAgent, HfApiModel,load_tool,tool
import datetime
import requests
import pytz
import yaml
from dotenv import load_dotenv
import os
from tools.final_answer import FinalAnswerTool

from Gradio_UI import GradioUI

load_dotenv()

auth = os.getenv("NANOLEAF_AUTH")
ip = os.getenv("NANOLEAF_IP")
port = os.getenv("NANOLEAF_PORT")

base_url = f"http://{ip}:{port}/api/v1/{auth}"

# Below is an example of a tool that does nothing. Amaze us with your creativity !
# @tool
# def my_custom_tool(arg1:str, arg2:int)-> str: #it's import to specify the return type
#     #Keep this format for the description / args / args description but feel free to modify the tool
#     """A tool that does nothing yet 
#     Args:
#         arg1: the first argument
#         arg2: the second argument
#     """
#     return "What magic will you build ?"

@tool
def nanoleaf_on() -> dict:
    """Turns on the Nanoleaf"""
    payload = {"on": {"value": True}}
    return send_to_nanoleaf_api("state", payload, "PUT")

@tool
def nanoleaf_off() -> dict:
    """Turns off the Nanoleaf"""
    payload = {"on": {"value": False}}
    return send_to_nanoleaf_api("state", payload, "PUT")

@tool
def set_nanoleaf_brightness(brightness: int) -> dict:
    """Sets the brightness of the Nanoleaf
    Args:
        brightness: The brightness value between 0 and 100
    """
    payload = {"brightness": {"value": brightness}}
    return send_to_nanoleaf_api("state", payload, "PUT")

@tool
def nanoleaf_color_temperature(temperature: int) -> dict:
    """Sets the color temperature of the Nanoleaf
    Args:
        temperature: The color temperature value between 1200 and 6500
    """
    payload = {"ct": {"value": temperature}}
    return send_to_nanoleaf_api("state", payload, "PUT")

@tool
def set_nanoleaf_color(hue: int, saturation: int, brightness: int) -> dict:
    """Sets the color of the Nanoleaf
    Args:
        hue: The hue value between 0 and 360
        saturation: The saturation value between 0 and 100
        brightness: The brightness value between 0 and 100
    """
    payload = {"hue": {"value": hue}, "sat": {"value": saturation}, "brightness": {"value": brightness}}
    return send_to_nanoleaf_api("state", payload, "PUT")

@tool
def set_nanoleaf_effect(effect: str) -> dict:
    """Sets the effect of the Nanoleaf
    Args:
        effect: The effect name
    """
    payload = {"select": effect}
    return send_to_nanoleaf_api("effects", payload, "PUT")

@tool
def get_nanoleaf_effects() -> list:
    """Gets the list of effects of the Nanoleaf"""
    return send_to_nanoleaf_api("effects/effectsList", {}, "GET")



def send_to_nanoleaf_api(endpoint, payload, method):
    headers = {
        'Content-Type': 'application/json'
    }
    url = f"{base_url}/{endpoint}"
    print(url)
    try:
        response = requests.request(method, url, headers=headers, json=payload)
        if response.status_code == 204:
            return {"message": "Success"}
        return response.json()
    except Exception as e:
        return {"error": str(e)}

    

final_answer = FinalAnswerTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 

model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
custom_role_conversions=None,
)


# Import tool from Hub
#image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True)

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
agent = CodeAgent(
    model=model,
    tools=[final_answer, nanoleaf_on, nanoleaf_off, nanoleaf_color_temperature, get_nanoleaf_effects, set_nanoleaf_effect, set_nanoleaf_color, set_nanoleaf_brightness], ## add your tools here (don't remove final answer)
    max_steps=6,
    verbosity_level=1,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    prompt_templates=prompt_templates
)


GradioUI(agent).launch()