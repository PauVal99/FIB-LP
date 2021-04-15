flatten :: [[Int]] -> [Int]

flatten list = foldr (++) [] list

myLength :: String -> Int

myLength string = sum $ map (const 1) string

myReverse :: [Int] -> [Int]

myReverse list = foldl (\xs x -> x:xs) [] list

countIn :: [[Int]] -> Int -> [Int]

countIn list needle = map (\xs -> length (filter (== needle) xs)) list

firstWord :: String -> String

firstWord text = takeWhile (/= ' ') (dropWhile (== ' ') text)