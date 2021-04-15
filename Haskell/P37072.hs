data Tree a = Node a (Tree a) (Tree a) | Empty 
    deriving (Show)

t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2

size :: Tree a -> Int

size Empty = 0
size (Node _ lt rt) = 1 + size lt + size rt

height :: Tree a -> Int

height Empty = 0
height (Node _ lt rt) = 1 + max (height lt) (height rt)

equal :: Eq a => Tree a -> Tree a -> Bool

equal Empty Empty = True
equal _ Empty = False
equal Empty _ = False
equal (Node t1 lt1 rt1) (Node t2 lt2 rt2)
    | t1 == t2 = equal lt1 lt2 && equal rt1 rt2
    | otherwise = False

isomorphic :: Eq a => Tree a -> Tree a -> Bool

isomorphic Empty Empty = True
isomorphic _ Empty = False
isomorphic Empty _ = False
isomorphic (Node t1 lt1 rt1) (Node t2 lt2 rt2) =
    t1 == t2 &&
    ((isomorphic lt1 lt2) && (isomorphic rt1 rt2) || (isomorphic lt1 rt2) && (isomorphic rt1 lt2))

preOrder :: Tree a -> [a]

preOrder Empty = []
preOrder (Node x l r) = x:(preOrder l ++ preOrder r)

postOrder :: Tree a -> [a]

postOrder Empty = []
postOrder (Node x l r) = (postOrder l) ++ (postOrder r) ++ [x]

inOrder :: Tree a -> [a]

inOrder Empty = []
inOrder (Node x l r) = inOrder l ++ x:inOrder r

breadthFirst :: Tree a -> [a]

breadthFirst t = bf [t]
    where 
        bf [] = []
        bf (Empty:ts) = bf ts
        bf ((Node x l r):ts) = x:bf (ts ++ [l,r])

build :: Eq a => [a] -> [a] -> Tree a

build [] [] = Empty
build p@(px : pxs) i = Node px (build lp li) (build rp ri)
  where (li,_:ri) = span (/=px) i
        (lp,rp) = splitAt (length li) pxs

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a

overlap _ Empty Empty = Empty
overlap _ t1 Empty = t1
overlap _ Empty t2 = t2
overlap f (Node t1 lt1 rt1) (Node t2 lt2 rt2) = Node (f t1 t2) (overlap f lt1 lt2) (overlap f rt1 rt2)