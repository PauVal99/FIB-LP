fizzBuzz :: [Either Int String]

fizzBuzz = map fb [0..]

fb :: Int -> Either Int String

fb x
    | x `mod` 15 == 0 = Right "FizzBuzz"
    | x `mod` 3 == 0 = Right "Fizz"
    | x `mod` 5 == 0 = Right "Buzz"
    | otherwise = Left x