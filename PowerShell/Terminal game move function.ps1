function TerminalMove([int] $pos, [int] $roll) {
  # your code here
  $posnew = $pos + 2 * $roll
  return $posnew
}