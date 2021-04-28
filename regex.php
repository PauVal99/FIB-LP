<?php
error_reporting(E_ALL ^ E_WARNING); 

function test($pattern, $tests) {
    echo "Pattern: $pattern\n\n";
    foreach($tests as $test)
        echo "\"$test\" ", preg_match($pattern, $test) ? '✔' : '❌', "\n";
}

switch ($argv[1]) {
    case 1:
        test(
            $pattern = '/^[a-zA-Z_][a-zA-Z0-9_]*$/',
            $tests = ['2A', 'a', '1', '_', 'A', 'ImAnId', 'ImNotAnId`', '``%$@', 'Hi_34']
        );
        break;
    case 2:
        test(
            $pattern = '/^[-+]?[0-9]*(\.[0-9]+)?(e[-+]?[0-9]+)?$/',
            $tests = ['', '3.1416', '-3e4', '+1.0e-5', '.567e+8', '111', '111.', '12.4e', 'ImNotFloating']
        );
        break;
    case 6:
        test(
            $pattern = '/^[0-9]*\.?[0-9]+?$/',
            $tests = ['', '3.1416', '111', '111.', 'ImNotFloating']
        );
        break;
    case 3:
        test(
            $pattern = '/^[ac]*(a[ac]*b[abc]*)?$/',
            $tests = ['', 'a', 'b', 'c', 'aa', 'acaac', 'cb', 'ab', 'acb', 'abcb', 'ccaccbaccb']
        );
        break;
    case 4:
        test(
            $pattern = '/^[b-df-hj-np-tv-z]*a[b-df-hj-np-tv-z]*e[b-df-hj-np-tv-z]*i[b-df-hj-np-tv-z]*o[b-df-hj-np-tv-z]*u[b-df-hj-np-tv-z]*$/',
            $tests = ['a', 'b', 'aei','aeiou', 'zfaehipojksuj', 'aetgvilkmdocur', 'aaeiou', 'gabecidoeuf', 'zfaaehipojksuj']
        );
        break;
    case 5:
        $pattern = '';
        foreach(range('a','z') as $char)
            $pattern .= "$char*";
        test(
            $pattern = '/^'.$pattern.'$/',
            $tests = ['a', 'ab', 'abc', 'acb', 'afhmnqsyz', 'abcdz','dgky', 'bdeaz']
        );
        break;
    default:
        echo "Invalid problem number.\n";
        break;
}
