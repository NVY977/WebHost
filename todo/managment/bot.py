from django.core.managmentBase import BaseComand
# from django.conf import settings
# from telegram import Bot
# from telegram.utils.request import Request
# from telegram import Update
# from telegram.ext import CallBackContext, Filters, MessageHandler, Updater


class Comand (BaseComand):
  help = "Telegram Bot"
  def handle (self, *args, **options):
    pass
    # request = Request(
    #   connect_timeout = 0.5,
    #   read_timeout = 1.0,
    # )
    # bot = Bot(
    #   request = request,
    #   token = settings.Token,
    #   base_url = settings.PROXY_URL,
    # )
    # print(bot.get_me())