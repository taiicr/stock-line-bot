# Stock Line Bot

This is a simple Line bot to fetch stock prices using Alpha Vantage API.

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/stock-line-bot.git
    cd stock-line-bot
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Create a `config.txt` file in the project root directory and add your credentials:
    ```txt
    LINE_CHANNEL_ACCESS_TOKEN=your_line_channel_access_token
    LINE_CHANNEL_SECRET=your_line_channel_secret
    ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
    ```

4. Run the application:
    ```sh
    python app.py
    ```

## Deployment

This bot can be deployed on render. Follow the steps:

1. Push the code to a GitHub repository.
2. Create a new Web Service on render and connect your GitHub repository.
3. Set the environment variables in render.
4. Deploy and get the service URL.
5. Set the Webhook URL in Line Developers console to `https://your-app.onrender.com/callback`.

## Usage

Add the Line bot as a friend and send a stock symbol (e.g., `AAPL`) to get the current stock price.
