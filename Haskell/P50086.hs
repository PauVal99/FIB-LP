data Queue a = Queue [a] [a]
     deriving (Show)
 
create :: Queue a

create = Queue [] []

push :: a -> Queue a -> Queue a

push x (Queue as bs) = Queue as (x:bs)

pop :: Queue a -> Queue a

pop (Queue [] []) = Queue [] []
pop (Queue [] bs) = Queue (reverse (init bs)) []
pop (Queue (a:as) bs) = Queue as bs

top :: Queue a -> a

top (Queue [] bs) = last bs 
top (Queue (a:as) bs) = a

empty :: Queue a -> Bool

empty (Queue [] []) = True
empty _ = False

instance Eq a => Eq (Queue a)
     where (Queue as1 bs1) == (Queue as2 bs2) = (as1 ++ reverse bs1) == (as2 ++ reverse bs2)

instance Functor Queue
    where
        fmap f (Queue as bs) = (Queue (fmap (f) as) (fmap (f) bs))

translation :: Num b => b -> Queue b -> Queue b

translation x queue = fmap (+x) queue

q2l :: (Queue a) -> [a]

q2l (Queue as bs) = (as ++ (reverse bs))

instance Applicative Queue
    where
        pure x = (Queue [x] [])
        f <*> queue = (Queue ((q2l f) <*> (q2l queue)) [])

instance Monad Queue
    where
        return x = (Queue [x] [])
        queue >>= f = (Queue l [])
            where
                l = (q2l queue) >>= (q2l . f)

kfilter :: (p -> Bool) -> Queue p -> Queue p
kfilter f queue = do
    q <- queue
    if (f q) then return q 
    else (Queue [] [])