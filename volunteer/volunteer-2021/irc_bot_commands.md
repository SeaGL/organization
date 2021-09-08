## IRC Bot Command Basics

We have an IRC bot named 'seagl-bot' that can help manage the conference in IRC. You can see what
commands are available by running `!help` in any channel that the bot is in (`#seagl-welcome` is a
good one to start in if you're not sure where to go).

You can find more complete [documentation for this bot
here](https://github.com/treedavies/seagl-2020-bot/blob/master/seagl-bot-doc)

This is a list of the commands available as of this writing:

### Available to everyone

```
!help                           - Print bot commands (this help text)
!schedule                       - Return URL to seagl2020 track schedule
!createroom (!cr) <room-name>   - Create channel and conference chat room         
!listrooms (!lr) <page-number>  - List Conference chat rooms                      
!jointopic (!jt) <topic-name>   - Join topic list, receive invites and announcements
!listtopics (!lt)               - List topics to join                             
!teagl (!tea) <nick>            - "TeaGL" toast someone (similar to ++)
!ask <question>                 - Send the Conference speaker a question
```

### Available to volunteers

```
!questions            - List questions asked by attendees
!clear_question_list  - Delete all questions asked to the channel to clear it before the next talk starts
```
