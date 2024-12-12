function Multi-Table ([int] $n) {
    return (1..10 | ForEach-Object { "$($_) * $($n) = $($_ * $n)"; }) -join "`n";
}