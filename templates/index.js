const TelegramBot = require('node-telegram-bot-api'); // подключаем node-
const token = '5130651792:AAFMydgoQOYD9qbqJI77ZzYtjb9itJEDHxY'; // тут токен 
// включаем самого обота
const bot = new TelegramBot(token, {polling: true});

// обработчик события присылания нам любого сообщения
bot.on('message', (msg) => {
  const chatId = msg.chat.id; //получаем идентификатор диалога, чтобы отвечать 

  // отправляем сообщение
  bot.sendMessage(chatId, 'Получили твое сообщение!');
});

