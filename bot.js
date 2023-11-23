const Discord = require('discord.js');
const client = new Discord.Client();
const token = 'MTE3Mjg1NzY4Nzk0ODY3NzE1MA.GBAio5.5A0Zx0T2KE6z4WuyH5M0X2NPGhftIVQFRRj0RA';

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

client.on('message', (msg) => {
  if (msg.content === 'ping') {
    msg.reply('Pong!');
  }
});

client.login(token);
