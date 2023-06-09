import os
# os.environ['DJANGO_SETTINGS_MODULE'] = 'PMP_model.settings'
# django.setup()

from telegram.ext import * 
from telegram import InputMediaPhoto
from telegram.ext import Updater
from telegram import Update

from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

API_KEY = '5908624943:AAHud2jZFdgS8hEtL3I_2YwxcjXjENXqNM0'

print("bot stated...")
idt=[767106459,767894205]

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello vishal')

async def vish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello ')

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'hiii i will to took u..')

# async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     id=update['message']['chat']['id']
#     name=update['message']['chat']['first_name']
#     uname=update['message']['chat']['username']
#     await update.message.reply_text(f"""User Info\nID:{id}\nFirst Name:{name}\nUsername:@{uname}""")

def val(update,context):
    return update.message.reply_text(f"i'm chat bot")

# max_id = int(mainamount.objects.aggregate(Max('id'))['id__max'])
# md = mainamount.objects.filter(id=max_id)
# for i in md:
#     value=i.amount
# cust=customers.objects.all().count()
# prod=product.objects.all().count()
# custname=[]
# cdatan=customers.objects.all()
# for i in cdatan:
#     custname.append(i.name)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    idtoken=update['message']['chat']['id']
    print(type(idtoken))
    
    if idtoken in idt:
        text = str(update.message.text).lower()
        txt={
            'hii':"hii i'm your bot...",
            'hello':"hello i'm your bot...",
            "vishal":"hiii vishal",
            'value':value,
            "customers":cust,
            "prodect":prod,
            "customer name":custname,
        }
        for i in txt.keys():
            if text==i:
                await update.message.reply_text(txt[i])
    else:
        await update.message.reply_text("nthink")


app = ApplicationBuilder().token(API_KEY).build()

app.add_handler(CommandHandler("hii",val))
# app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("yes",vish))
app.add_handler(CommandHandler("info",info))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()