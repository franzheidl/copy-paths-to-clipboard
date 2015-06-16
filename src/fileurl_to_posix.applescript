-- set q to "file:///Users/franz/Library/Application Support/Alfred 2/Alfred.alfredpreferences/workflows/user.workflow.79AA6A1F-DEB4-44B0-8ADC-837BAA98B9A9/copyallpaths_main.py, file:///Users/franz/Library/Application Support/"

on run(q)
  set theTargets to {}
  set oldItemDelimiters to text item delimiters
  set text item delimiters to ", "
  set qList to every text item of (q as text)
  set text item delimiters to oldItemDelimiters
  repeat with aTarget in qList
    if aTarget starts with "file://localhost" then
      set aTarget to my doSed(aTarget, "s|file://localhost\\(.*\\)|\\1|")
    else
      set aTarget to my doSed(aTarget, "s|file://\\(.*\\)|\\1|")
    end if
    set theTargets to theTargets & aTarget
  end repeat
  return (theTargets)
end run

on doSed(theString, thePattern)
  do shell script "echo " & quoted form of theString & " |" & "sed '" & thePattern & "'"
end doSed
