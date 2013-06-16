-- Copy Paths to Clipboard
-- Workflow For Alfred 2
-- Franz Heidl 2013
-- http://github.com/franzheidl/copy-paths-to-clipboard
-- MIT license.
--
-- Method to get the path of the frontmost document from this gist by Clinton Strong:
-- https://gist.github.com/clintxs/5260225


on run
	tell application "System Events"
		set theTarget to ""
		set theApp to the the name of the first process whose frontmost is true
				
		if theApp is "Finder" then
			tell application "Finder"
				try
					set theSelection to (get selection)
					if length of theSelection is 1 then
						set theTarget to POSIX path of (item 1 of theSelection as text)
					else
						set theTarget to ""
						repeat with anItem in theSelection
							if length of theTarget is greater than 0 then
								set theTarget to theTarget & ", "
							end if
							set theTarget to theTarget & (POSIX path of (anItem as text))
						end repeat
					end if
				on error
					try
						set theTarget to POSIX path of (target of window 1 as text)
					on error
						set theTarget to ""
					end try
				end try
			end tell
		else
			try
				tell process theApp
					repeat with x from 1 to (count windows)
						try
							set theDoc to value of attribute "AXDocument" of window x
							set theFile to do shell script "php -r 'echo urldecode(\"" & theDoc & "\");'"
							set theTarget to my doSed(theFile, "s|file://localhost\\(.*\\)|\\1|")
							exit repeat
						end try
					end repeat
				end tell
			end try
		end if
	end tell
	return {theTarget}
end run


on doSed(theString, thePattern)
	do shell script "echo " & quoted form of theString & " |" & "sed '" & thePattern & "'"
end doSed
