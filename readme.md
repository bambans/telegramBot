# telegramBot

This is a simple Telegram bot API implementation in Python3.

## Usage

1. Configure your bot and get your ``<api token>`` (See [Telegram Bots](https://core.telegram.org/bots));
2. Go to line 6 in ``telegram.py`` and paste your token in ``apiToken`` variable;
3. Configure your message in ``sendToTelegram(<chatID>, <message>)``;

## How does it work?

Once people send messages to your bot (like the default first one ``/start``), your bot can get updates (see the response object) with some user data. Hence, you can filter the data by ``username`` and get the chat or user ``ìd``, what you may use to send your messages from your bot to a specific user.