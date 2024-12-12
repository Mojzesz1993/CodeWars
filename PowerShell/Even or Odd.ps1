function Get-EvenOrOdd($number) {
  if ($number % 2 -eq 0) {
    Write-output "Even"
  }
  else {
    Write-output "Odd"
  }
}