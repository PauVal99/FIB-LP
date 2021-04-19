<?php

function split($delimiter, $string) {
    $splited = explode($delimiter, $string, $limit = 2);
    if($splited[0] == $string)
        return false;
    return $splited;
}

function parse($expression) {
    $expression = str_replace(' ', '', $expression);
    $expression = str_replace('-', '+-', $expression);
    return $expression;
}

function operate($expression) {
    foreach(['+', '/', '*'] as $operation) {
        if($expressions = split($operation, $expression))
            switch ($operation) {
                case '+':
                    return operate($expressions[0]) + operate($expressions[1]);
                case '*':
                    return operate($expressions[0]) * operate($expressions[1]);
                default:
                    return operate($expressions[0]) / operate($expressions[1]);
            }
    }
    return $expression;
}

function evaluate($expression) {
    return operate(parse($expression));
}

while(true)
    echo evaluate(readline()), "\n";