# CountdownBot

You read the tile; it does what it says, using little code to operate totally on a cheap TV box.

# Requirements
I do not know for sure. This works perfectly on the Oranth Tanix TX3 Mini running Ubuntu 20.04.1 LTS (aarch64).

# Tutorial
(Side note: I made this around 1:30 a.m., so please pardon my grammar mistakes. Thanks)
1. Install Python 3, Discord.py, Datetime, and Pytz. (I don't think you need me to teach you these, right?)
2. 'git clone' everything
3. Get into the 'src' folder
4. nano 'main.py', then replace these as follows:
- Replace "YOUR_BOT_ID" with the Discord bot ID. You know where to get it, right?
- Replace "YOUR_CHANNEL_ID" with the channel ID that you want the bot to text on; you know where to find it, right?
- Replace "user_id" with your own or others' user_id, and you know where to find it, right?
5. Run the bot using python3 main.py, let it run for a few seconds, and it should be good to go.
  (Side note: You know it's functioning when it pings you the message counting down the time left in days.)
