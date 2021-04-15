absValue :: Int -> Int

absValue n
    | n >= 0 = n
    | otherwise = -n

power :: Int -> Int -> Int

power x p = product (take p (repeat x))

isPrime :: Int -> Bool

isPrime 0 = False
isPrime 1 = False
isPrime n = not (hasDivisors n 2)

hasDivisors :: Int -> Int -> Bool

hasDivisors n divisor
    | divisor * divisor > n = False
    | mod n divisor == 0 = True
    | otherwise = hasDivisors n (divisor + 1)

slowFib :: Int -> Int

slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n - 1) + slowFib (n - 2)

quickFib :: Int -> Int

quickFib n = quickFib' 0 1 n

quickFib' :: Int -> Int -> Int -> Int

quickFib' a b 0 = a
quickFib' a b iteration = quickFib' b (a + b) (iteration - 1)