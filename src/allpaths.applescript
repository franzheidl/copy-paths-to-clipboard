on run
  tell application "System Events"
    set theTargets to ""
    set theApp to the name of the first process whose frontmost is true
    
    if theApp is "Finder" then
      tell application "Finder"
        try
          set theSelection to (get selection as alias list)
          repeat with anItem in theSelection
            tell application "system Events" to set anItem to URL of anItem
            if theTargets is "" then
              set theTargets to anItem
            else
              set theTargets to theTargets & ", " & anItem
            end if
          end repeat
        on error
          try
            tell application "System Events" to set theUrl to URL of (target of window 1 as text)
            if theUrl is missing value then
              set theTargets to ""
            else
              set theTargets to theUrl
            end if
          on error
            set theTargets to ""
          end try
        end try
      end tell
      
    else
      tell process theApp
        
        repeat with x from 1 to (count windows)
          try
            set theDoc to the value of attribute "AXDocument" of window x
            if theDoc is not missing value then
              if the length of theTargets is 0 then
                set theTargets to theDoc
              else
                set theTargets to theTargets & ", " & theDoc
              end if
            end if
          end try
        end repeat
        
      end tell
    end if
        
  end tell
  return {theTargets}
end run
