from smolagents import CodeAgent, HfApiModel, load_tool
import yaml
from tools.final_answer import FinalAnswerTool
from tools.nanoleaf_tools import (
    nanoleaf_on,
    nanoleaf_off,
    set_nanoleaf_brightness,
    nanoleaf_color_temperature,
    set_nanoleaf_color,
    set_nanoleaf_effect,
    get_nanoleaf_effects
)
from Gradio_UI import GradioUI

final_answer = FinalAnswerTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 

model = HfApiModel(
max_tokens=2096,
temperature=0.5,
model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
custom_role_conversions=None,
)

# Load the prompt templates from a YAML file
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