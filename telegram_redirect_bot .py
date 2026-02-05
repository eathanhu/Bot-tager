import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Replace with your bot token from @BotFather
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for /start command to check if bot is working"""
    await update.message.reply_text(
        "✅ Bot is working!\n"
        "I will redirect users to the new channel when they message in groups."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler for all messages in group chats"""
    # Check if message is from a group or supergroup (not DM)
    if update.message.chat.type in ['group', 'supergroup']:
        user = update.message.from_user
        
        # Get username or first name for tagging
        if user.username:
            user_tag = f"@{user.username}"
        else:
            user_tag = f"[{user.first_name}](tg://user?id={user.id})"
        
        # Send redirect message
        await update.message.reply_text(
            f"{user_tag}, This channel is closed please join my another channel",
            parse_mode='Markdown'
        )

def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(
        filters.ALL & ~filters.COMMAND,  # All messages except commands
        handle_message
    ))
    
    # Start the bot
    print("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
