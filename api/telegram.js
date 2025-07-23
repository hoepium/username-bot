const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const { getUsernamePrice, checkUsernameValidity } = require('../utils/pricing');
const { roastUsername } = require('../utils/roast');

const app = express();
app.use(bodyParser.json());

app.post('/', async (req, res) => {
  try {
    const body = req.body;
    if (!body.message || !body.message.text) {
      return res.sendStatus(200);
    }

    const text = body.message.text.trim();
    const chatId = body.message.chat.id;

    let reply = '';

    if (text.startsWith('/rate')) {
      const match = text.match(/@?([a-zA-Z0-9_]+)/);
      if (!match) {
        reply = 'Please provide a valid username.';
      } else {
        const username = match[1];
        const validity = checkUsernameValidity(username);
        if (validity !== true) {
          reply = validity;
        } else {
          const result = getUsernamePrice(username);
          // Defensive: Ensure price/reason exist
          if (!result || typeof result.price === 'undefined' || typeof result.reason === 'undefined') {
            reply = 'Could not compute price for this username.';
          } else {
            const { price, reason } = result;
            reply = @${username} — Estimated value: $${price} USD\n${reason};
          }
        }
      }
    } else if (text.startsWith('/roast')) {
      const match = text.match(/@?([a-zA-Z0-9_]+)/);
      if (!match) {
        reply = 'Please provide a valid username to roast.';
      } else {
        reply = roastUsername(match[1]);
      }
    } else {
      reply = 'Unknown command. Use /rate @username or /roast @username.';
    }

    // Telegram sendMessage API
    await axios.post(
      https://api.telegram.org/bot${process.env.BOT_TOKEN}/sendMessage,
      { chat_id: chatId, text: reply }
    );
    res.sendStatus(200);

  } catch (error) {
    // Log and handle errors for consistent debugging
    console.error("Bot handler error:", error);
    res.sendStatus(200); // Always respond with 200 to Telegram
  }
});

module.exports = app;
