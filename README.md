# Nanoleaf Agent

This project demonstrates how to create a custom AI agent using the `smolagents` library and integrate it with Gradio for a user-friendly interface. The purpose of this app is to provide an interactive platform where users can communicate with the AI agent to control and interact with their Nanoleaf devices. By leveraging the capabilities of the `smolagents` library and the simplicity of Gradio, this project aims to offer an intuitive and efficient way to manage smart lighting systems.

## Project Structure

- `app.py`: Main application file that sets up the agent and its tools.
- `Gradio_UI.py`: Contains the Gradio UI implementation for interacting with the agent.
- `tools/`: Directory containing custom tools used by the agent.
    - `final_answer.py`
    - `nanoleaf_tools.py`
- `agent.json`: Configuration file for the agent.
- `prompts.yaml`: YAML file containing prompt templates for the agent.
- `requirements.txt`: List of dependencies required for the project.
- `.gitattributes`: Git LFS configuration file.
- `README.md`: This file.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:
     ```sh
     git clone <repository-url>
     cd <repository-directory>
     ```
2. Install the required dependencies:
        ```sh
        pip install -r requirements.txt
        ```

3. Create a `.env` file and include your Nanoleaf device's IP address and port:
        ```sh
        NANOLEAF_IP=<your-nanoleaf-ip>
        NANOLEAF_PORT=<your-nanoleaf-port>
        NANOLEAF_AUTH=<your-nanoleaf-auth-code>
        ```
     You can get the auth code from your device. [Nanoleaf API Docs](https://forum.nanoleaf.me/docs#_8qk4k7xuzlc9)

4. Run the application:
        ```sh
        python app.py
        ```

## Usage

Once the application is running, you can interact with the AI agent through the Gradio interface. The interface allows you to input queries and receive responses from the agent. Here are some cool things you can do with the app:

- **Control Your Lights**: Easily turn your Nanoleaf lights on or off, change colors, and adjust brightness with simple commands.
- **Create Ambiance**: Tell the agent what mood you want and let it choose a color or effect to match.
- **Display Messages in Morse Code**: Have the agent translate your text into Morse code and display it using your Nanoleaf lights.
- **Interactive Light Shows**: Create dynamic light shows based on your commands or even based on the content of your conversations with the agent.

With the intuitive Gradio interface, managing your Nanoleaf devices has never been easier or more enjoyable!

## Customization

You can customize the agent by modifying the tools in the `tools/` directory or updating the prompt templates in `prompts.yaml`. Adjust the `agent.json` configuration file to change the agent's settings.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
        ```sh
        git checkout -b feature-branch
        ```
3. Make your changes and commit them:
        ```sh
        git commit -m "Description of changes"
        ```
4. Push to the branch:
        ```sh
        git push origin feature-branch
        ```
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This project is built off of the [First Agent Template](https://huggingface.co/spaces/agents-course/First_agent_template) from Hugging Face's AI Agent Course.