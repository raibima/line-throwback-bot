from flask import Flask, request, abort
from linebot import (
  LineBotApi, WebhookHandler
)
from linebot.exceptions import (
  InvalidSignatureError
)
from linebot.models import (
  MessageEvent, TextMessage, ImageSendMessage
)
from os import environ
from random_photo import random_photo

app = Flask(__name__)
line_bot_api = LineBotApi(environ['CHANNEL_TOKEN'])
handler = WebhookHandler(environ['CHANNEL_SECRET'])

@app.route('/callback', methods=['POST'])
def callback():
  # get X-Line-Signature header value
  signature = request.headers['X-Line-Signature']

  # get request body as text
  body = request.get_data(as_text=True)
  app.logger.info("Request body: " + body)

  # handle webhook body
  try:
    handler.handle(body, signature)
  except InvalidSignatureError:
    abort(400)

  return 'OK'

def send_random_photo(reply_token):
  photo = random_photo()
  line_bot_api.reply_message(
    reply_token,
    ImageSendMessage(
      original_content_url=photo,
      preview_image_url=photo
    )
  )

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  message = event.message.text.strip()
  if message == '/throwback':
    send_random_photo(event.reply_token)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=(environ['PORT'] or 5000))