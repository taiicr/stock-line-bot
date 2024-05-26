import os
import requests
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage


# 加载 config.txt 文件中的环境变量
def load_config_file(filepath):
    with open(filepath) as f:
        for line in f:
            name, value = line.strip().split('=', 1)
            os.environ[name] = value


# 加载 config.txt 文件中的环境变量
load_config_file('config.txt')

app = Flask(__name__)

# 从环境变量中获取 LINE bot 的凭证和 Alpha Vantage API 密钥
line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))
alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')


@app.route("/callback", methods=['POST'])
def callback():
    # 获取请求的签名
    signature = request.headers['X-Line-Signature']
    # 获取请求的主体
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # 验证签名
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    stock_symbol = event.message.text.upper()
    stock_price = get_stock_price(stock_symbol)

    if stock_price:
        reply_text = f"The current price of {stock_symbol} is {stock_price} USD."
    else:
        reply_text = "Sorry, I couldn't retrieve the stock price. Please check the stock symbol."

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )


def get_stock_price(symbol):
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={alpha_vantage_api_key}"
    response = requests.get(url)
    data = response.json()
    if "Global Quote" in data:
        return data["Global Quote"]["05. price"]
    return None


if __name__ == "__main__":
    app.run()
