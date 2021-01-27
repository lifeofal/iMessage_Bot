on run {targetPhoneNumber, targetMessageToSend}

launch application "Messages"

tell application "Messages"

	set targetService to 1st account whose service type = iMessage
	--set targetPhoneNumber to "Parker Landers"
	--set targetMessageToSend to "Test"
	set isName to true
	


	if isName is true then
		set targetMessageToSend to "string"
		--set targetName to get id of account of participant "Alejandro Cervantes"
		tell application "Contacts"

			set theContact to the first person whose name is targetPhoneNumber
			set targetPhoneNumber to value of first phone of theContact as text
			--set targetBuddy to participant targetPhoneNumber of targetService
		end tell

	end if
	set targetBuddy to participant targetPhoneNumber of targetService


	set targetMessage to targetMessageToSend
	send targetMessage to targetBuddy

end tell
end run
