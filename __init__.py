from .telegram_sender import TelegramSender

NODE_CLASS_MAPPINGS = {"TelegramSender": TelegramSender}
NODE_DISPLAY_NAME_MAPPINGS = {"TelegramSender": "Telegram Sender"}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']