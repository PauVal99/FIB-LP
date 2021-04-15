insert :: [Int] -> Int -> [Int]

insert [] n = [n]
insert (head:tail) n 
    | head > n = n:head:tail
    | otherwise = head:(insert tail n)

isort :: [Int] -> [Int]

isort [] = []
isort (head:tail) = insert (isort tail) head

remove :: [Int] -> Int -> [Int]

remove [] n = []
remove (head:tail) n
    | head == n = tail
    | otherwise = head:(remove tail n)

ssort :: [Int] -> [Int]

ssort [] = []
ssort list = min:ssort(remove list min)
    where min = minimum list

merge :: [Int] -> [Int] -> [Int]

merge [] [] = []
merge list [] = list
merge [] list = list
merge (x:xs) (y:ys)
    | x < y = x:(merge xs (y:ys))
    | otherwise = y:(merge (x:xs) ys)

msort :: [Int] -> [Int]

msort [] = []
msort [element] = [element]
msort list = merge (msort (fst sliced)) (msort (snd sliced))
    where sliced = split list

split :: [Int] -> ([Int], [Int])

split [] = ([],[])
split list = splitAt (((length list) + 1) `div` 2) list

qsort :: [Int] -> [Int]

qsort [] = []
qsort (x:xs) = (qsort (smaller xs x)) ++ (x:(qsort (greater xs x)))

genQsort :: Ord a => [a] -> [a]

genQsort [] = []
genQsort (x:xs) = (genQsort (smaller xs x)) ++ (x:(genQsort (greater xs x)))

smaller :: Ord a => [a] -> a -> [a]

smaller [] _ = []
smaller list x = [n | n <- list, n <= x]

greater :: Ord a => [a] -> a -> [a]

greater [] _ = []
greater list x = [n | n <- list, n > x]
