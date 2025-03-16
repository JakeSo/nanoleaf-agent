from smolagents import tool
import requests
from dotenv import load_dotenv
import os

load_dotenv()
auth = os.getenv("NANOLEAF_AUTH")
ip = os.getenv("NANOLEAF_IP")
port = os.getenv("NANOLEAF_PORT", 16021)  # Default port for Nanoleaf API is usually 16021, but you can change it if needed

base_url = f"http://{ip}:{port}/api/v1/{auth}"

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