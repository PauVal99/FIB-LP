eql :: [Int] -> [Int] -> Bool

eql list1 list2 = (length list1 == length list2) && (and (zipWith (==) list1 list2))

prod :: [Int] -> Int

prod list = foldr (*) 1 list

prodOfEvens :: [Int] -> Int

prodOfEvens list = prod (filter even list)

powersOf2 :: [Int]

powersOf2 = iterate (*2) 1

scalarProduct :: [Float] -> [Float] -> Float

scalarProduct vec1 vec2 = sum $ zipWith (*) vec1 vec2