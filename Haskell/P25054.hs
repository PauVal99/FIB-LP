myLength :: [Int] -> Int

myLength [] = 0
myLength list = 1 + myLength (tail list)

myMaximum :: [Int] -> Int

myMaximum [one] = one
myMaximum (first:second:list)
    | first > second = myMaximum (first:list)
    | otherwise = myMaximum (second:list)

average :: [Int] -> Float

average list = fromIntegral (sum list) / fromIntegral (length list)

buildPalindrome :: [Int] -> [Int]

buildPalindrome list = (reverse list) ++ list

remove :: [Int] -> [Int] -> [Int]

remove [] _ = []
remove (first:haystack) needle
    | first `elem` needle = remove haystack needle
    | otherwise = first : (remove haystack needle)

flatten :: [[Int]] -> [Int]

flatten [] = []
flatten list = (head list) ++ flatten (tail list)

oddsNevens :: [Int] -> ([Int],[Int])

oddsNevens [] = ([],[])
oddsNevens (first:list)
    | odd first = (first : fst next, snd next) 
    | otherwise = (fst next, first : snd next)
    where
        next = oddsNevens list

primeDivisors :: Int -> [Int]

primeDivisors n = [divisor | divisor <- [1..n], mod n divisor == 0, isPrime divisor]

isPrime :: Int -> Bool

isPrime 0 = False
isPrime 1 = False
isPrime n = not (hasDivisors n 2)

hasDivisors :: Int -> Int -> Bool

hasDivisors n divisor
    | divisor * divisor > n = False
    | mod n divisor == 0 = True
    | otherwise = hasDivisors n (divisor + 1)

intSqrt :: Int -> Int

intSqrt n = round (sqrt (fromIntegral n))