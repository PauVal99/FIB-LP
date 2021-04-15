myFoldl :: (a -> b -> a) -> a -> [b] -> a

myFoldl _ a [] = a
myFoldl f a (b:bs) = myFoldl f (f a b) bs

myFoldr :: (a -> b -> b) -> b -> [a] -> b

myFoldr _ b [] = b
myFoldr f b (a:as) = f a (myFoldr f b as)

myIterate :: (a -> a) -> a -> [a]

myIterate f a = a:(myIterate f (f a))

myUntil :: (a -> Bool) -> (a -> a) -> a -> a

myUntil c f x
    | c x = x
    | otherwise = myUntil c f (f x)

myMap :: (a -> b) -> [a] -> [b]

myMap f xs = myFoldr (\c i -> (f c):i) [] xs

myFilter :: (a -> Bool) -> [a] -> [a]

myFilter f xs = myFoldr (\c i -> if f c then c:i else i) [] xs

myAll :: (a -> Bool) -> [a] -> Bool

myAll f xs = myFoldr (\current acumulated -> (f current) && acumulated) True xs
--myAll f xs = and $ map f xs

myAny :: (a -> Bool) -> [a] -> Bool

myAny f xs = myFoldr (\current acumulated -> (f current) || acumulated) False xs
--myAny f xs = or $ map f xs

myZip :: [a] -> [b] -> [(a, b)]

myZip [] _ = []
myZip _ [] = []
myZip (x:xs) (y:ys) = (x,y):(myZip xs ys)

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]

myZipWith f xs ys = myFoldr (\(x, y) a -> (f x y):a) [] (myZip xs ys)