const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(bodyParser.json());

app.post('/', async (req, res) => {
  try {
    await axios.post(
      https://api.telegram.org/bot${process.env.BOT_TOKEN}/sendMessage,
      { chat_id: 1, text: "Test message" }
    );
    res.sendStatus(200);
  } catch (error) {
    console.error(error);
    res.sendStatus(200);
  }
});

module.exports = app;
