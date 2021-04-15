main = do
    line <- getLine
    if line /= "*" then do
        let ws = words line
        let name = ws !! 0
        let m = read $ ws !! 1
        let h = read $ ws !! 2
        putStrLn (name ++ ": " ++ (message $ index m h))
        main
    else
        return ()

message index
    | index < 18 = "magror"
    | index < 25 = "corpulencia normal"
    | index < 30 = "sobrepes"
    | index < 40 = "obesitat"
    | otherwise = "obesitat morbida"

index m h = m/(h^2)