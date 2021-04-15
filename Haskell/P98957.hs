ones :: [Integer]

ones = 1:ones

nats :: [Integer]

nats = iterate (+1) 0

ints :: [Integer]

ints = iterate (\x -> if x > 0 then -x else -x+1) 0

triangulars :: [Integer]

triangulars = 0:(scanl (+) 1 [2..])

factorials :: [Integer]

factorials = scanl (*) 1 [1..]

fibs :: [Integer]

fibs = scanl (+) 0 (1:fibs)

primes :: [Integer]

primes = garbell [2..]
    where
        garbell (p : xs) = p : garbell [x | x <- xs, x `mod` p /= 0]

hammings :: [Integer]

hammings = 1 : map (2*) hammings `merge` map (3*) hammings `merge` map (5*) hammings
  where merge (x:xs) (y:ys)
          | x < y = x : xs `merge` (y:ys)
          | x > y = y : (x:xs) `merge` ys
          | otherwise = x : xs `merge` ys

look :: [Char] -> Integer

look [] = 0
look [_] = 1
look (c1:c2:s)
    | c1 == c2 = 1 + (look (c2:s))
    | otherwise = 1

say :: [Char] -> [Char]

say [] = []
say s = (show count) ++ (head s) : (say (drop (fromIntegral count) s)) where count = look s

lookNsay :: [Integer]

lookNsay = iterate (read . say . show) 1

tartaglia :: [[Integer]]

tartaglia = iterate next [1]
    where next xs = zipWith (+) ([0] ++ xs) (xs ++ [0])