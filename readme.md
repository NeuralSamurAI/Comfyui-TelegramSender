# ComfyUI Telegram Sender Node

The ComfyUI Telegram Sender Node is a custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to send generated images and text messages to Telegram chats and channels using a Telegram bot.

## Features

- Send generated images to Telegram chats and channels
- Include formatted text captions with the images
- Support for various image formats: PNG, JPEG, WebP, GIF, TIFF
- Customize image compression levels and quality settings
- Format text using Telegram's markdown syntax (bold, italic, code, strikethrough, underline, spoiler)
- Send messages silently without triggering notifications
- Protect the content of sent messages

## Installation

1. Make sure you have ComfyUI installed and set up.

2. Install the required dependencies by running the following command:
```pip install python-telegram-bot```

3. Clone this repository or download the `telegram_sender.py` file.

4. Place the `telegram_sender.py` file in the `custom_nodes` directory of your ComfyUI installation.

## Configuration

1. Create a Telegram bot and obtain its token. You can follow the instructions in the [Telegram Bot API documentation](https://core.telegram.org/bots#creating-a-new-bot).

2. Create a `settings.json` file in the same directory as the `telegram_sender.py` file with the following content:
```json
{
  "telegram_bot_token": "YOUR_TELEGRAM_BOT_TOKEN"
}```

Replace "YOUR_TELEGRAM_BOT_TOKEN" with the actual token of your Telegram bot.

## Usage

In ComfyUI, add the TelegramSender node to your workflow.

Connect the generated images to the images input of the TelegramSender node.

Configure the node settings:
--chat_id: The ID of the Telegram chat where the images and messages will be sent. You can obtain the chat ID by sending a message to your bot and then making a request to the following URL:
    ```https://api.telegram.org/bot<YOUR_TELEGRAM_BOT_TOKEN>/getUpdates```
    Look for the chat_id field in the response.

--enable_image: Set to "True" to enable sending images.

--enable_text: Set to "True" to enable sending text captions with the images.

--text: Enter the text caption for the images. You can use Telegram's markdown syntax for formatting.

--bold, italic, code, strikethrough, underline, spoiler: Set to "True" to apply the respective formatting to the text.

--enable_channel: Set to "True" to enable sending messages to Telegram channels.

--channel_ids: Enter the IDs of the Telegram channels, separated by commas, where the messages will be sent.

--disable_notification: Set to "True" to send messages silently without triggering notifications.

--protect_content: Set to "True" to protect the content of sent messages.

--image_format: Select the desired image format from the dropdown menu (PNG, JPEG, WebP, GIF, TIFF).

--png_compress_level, jpeg_quality, webp_lossless, webp_quality: Customize the compression levels and quality settings for the respective image formats.

--Run the workflow, and the generated images and text messages will be sent to the specified Telegram chats and channels.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.