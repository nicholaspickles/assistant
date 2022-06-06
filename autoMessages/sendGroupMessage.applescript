on run {theGroup, targetMessage}
    tell application "Messages"
        set myid to theGroup
        set theBuddy to a reference to chat id myid
        send targetMessage to theBuddy
    end tell
end run