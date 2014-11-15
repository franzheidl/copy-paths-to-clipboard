on run(q)
  set theURLs to ""
  set oldItemDelimiters to text item delimiters
  set text item delimiters to ", "
  set qList to every text item of (q as text)
  set text item delimiters to oldItemDelimiters
  repeat with aTarget in qList
    set aTarget to (POSIX file aTarget as alias)
    tell application "System Events" to set aTarget to URL of aTarget
    if theURLs is "" then
      set theURLs to aTarget
    else
      set theURLs to theURLs & ", " & aTarget
    end if
  end repeat
  return (theURLs)
end run
