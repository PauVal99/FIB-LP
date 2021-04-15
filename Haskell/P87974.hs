main = do
    name <- getLine
    putStrLn $ "Hola " ++ (funnier name) ++ "!"

funnier name
    | last name == 'a' = "maca"
    | last name == 'A' = "maca"
    | otherwise = "maco"