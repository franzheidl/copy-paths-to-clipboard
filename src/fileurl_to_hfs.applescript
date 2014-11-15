on run(q)
  set theTargets to {}
  set oldItemDelimiters to text item delimiters
  set text item delimiters to ", "
  set qList to every text item of (q as text)
  set text item delimiters to oldItemDelimiters
  repeat with aTarget in qList
    set aTarget to (POSIX file aTarget)
    set theTargets to theTargets & (aTarget as text)
  end repeat
  return (theTargets)
end run