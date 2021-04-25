{-# LANGUAGE RecordWildCards #-}    -- per utilitzar fields

import Data.Char (isUpper)
import Data.List (nub, isInfixOf)
import Data.List.Split (splitOn)    -- cal instal·lar: cabal install split
import Data.String.Utils (strip)    -- cal instal·lar: cabal install MissingH
import Data.Maybe (isJust, mapMaybe, fromMaybe)

type Programa = [ Regla ]
type Sustitucio = [ (Term, Term) ]
type BaseConeixement = [ Atom ]

data Regla = Regla { _cap::Atom, _cos::[ Atom ] }
    deriving (Eq, Show)
data Atom = Atom { _nomPredicat::String, _termes::[ Term ] }
    deriving (Eq, Show)
data Term = Var String | Sym String
    deriving (Eq, Show)

{-  Autor: Pau Val 
    Dni: 46470753N 
    
    Notes:

    El programa crea correctament la base del coneixement amb regles amb un unic atom com a cos.
    Per contra, no crea del tot be la base del coneixement amb multiples atoms en regles i deriva en solucions erroneas.
    Les consultes sense variables i un atom funcionen. Per lo general es deixa algunes sustitucions posibles en consultes amb variables.
    Les consultes amb multiples atoms no van gaire be, la funcio d'avaluacio esta reusada i dona els mateixos problemes.

    Segurament el que causa aquests errors es a partir de avaluaAtom on no gestiono be les sustitucions encadenades.

    Al final deixo alguns jocs de proves que funcionen.
-}

main = do
    contents <- getContents
    let input = splitOn ["end."] (lines contents)
    let baseConeixement = createBaseConeixement (parsePrograma $ unlines (input !! 0))
    putStrLn $ unlines $ map (see) (evaluateQueries baseConeixement (unlines (input !! 1)))

see [] = "False"
see [[]] = "True"
see result = show result

-- Parser

parsePrograma :: String -> Programa
parsePrograma programa = map (parseRegla) (map (init) (lines programa))

splitCap regla = unwords $ tail $ (dropWhile (/= "=>") (words regla))

splitCos regla = map (unwords) (splitOn ["&"] (takeWhile (/= "=>") (words regla)))

parseRegla regla
    | isInfixOf "=>" regla = Regla (parseAtom $ splitCap regla) (map (parseAtom) (splitCos regla))
    | otherwise = Regla (parseAtom regla) []

parseAtom atom = Atom (head $ words atom) (map (parseTerm) (tail $ words atom))

parseTerm term
    | isUpper $ head term = (Var term)
    | otherwise = (Sym term)

-- BaseConeixement

fets programa = [_cap atom | atom <- programa, null $ _cos atom]

regles programa = [regla | regla <- programa, not.null $ _cos regla]

createBaseConeixement :: Programa -> BaseConeixement
createBaseConeixement programa = loopBaseConeixement (fets programa) (regles programa)

loopBaseConeixement baseConeixement [] = baseConeixement
loopBaseConeixement baseConeixement (regla:regles)
    | baseConeixement == (avaluaRegla baseConeixement regla) = baseConeixement
    | otherwise = loopBaseConeixement (avaluaRegla baseConeixement regla) regles

avaluaRegla :: BaseConeixement -> Regla -> BaseConeixement
avaluaRegla baseConeixement regla = nub (baseConeixement ++ (map (sustitueix (_cap regla)) (avaluaSustitucions baseConeixement [] (_cos regla))))

avaluaSustitucions :: BaseConeixement -> [ Sustitucio ] -> [ Atom ] -> [ Sustitucio ]
avaluaSustitucions baseConeixement sustitucions [] = sustitucions
avaluaSustitucions baseConeixement sustitucions (atom:atoms) = avaluaSustitucions baseConeixement (avaluaAtom baseConeixement atom sustitucions) atoms

avaluaAtom :: BaseConeixement -> Atom -> [ Sustitucio ] -> [ Sustitucio ]
avaluaAtom baseConeixement atom [] = mapMaybe (unifica atom) baseConeixement
avaluaAtom baseConeixement atom (sustitucio:sustitucions) = mapMaybe (unifica (sustitueix atom sustitucio)) baseConeixement ++ avaluaAtom baseConeixement atom sustitucions

-- Sustitucio

sustitueix :: Atom -> Sustitucio -> Atom
sustitueix atom sustitucio = Atom (_nomPredicat atom) (mapMaybe (\terme -> if isJust (lookup terme sustitucio) then lookup terme sustitucio else Just terme) (_termes atom))

-- Unificacio

unificable ((Sym terme1), (Sym terme2))
    | terme1 == terme2 = True
    | otherwise = False

unificable ((Var terme1), (Sym terme2)) = True
unificable (_, (Var terme)) = False

unificaTerm ((Sym terme1), (Sym terme2)) = Nothing
unificaTerm ((Var terme1), (Sym terme2)) = Just (Var terme1, Sym terme2)

uniqueSustitucio [] = True
uniqueSustitucio sustitucions = and $ map (\sustitucio -> uniqueVar sustitucio sustitucions) sustitucions  

uniqueVar (var, sym) [] = True
uniqueVar (var, sym) ((susVar, susSym):sustitucions)
    | var == susVar && sym /= susSym = False
    | otherwise = uniqueVar (var, sym) sustitucions

unifica :: Atom -> Atom -> Maybe Sustitucio
unifica (Atom predicat1 termes1) (Atom predicat2 termes2)
    | predicat1 /= predicat2 = Nothing
    | not $ and $ map (unificable) (zip termes1 termes2) = Nothing
    | not (uniqueSustitucio (mapMaybe (unificaTerm) (zip termes1 termes2))) = Nothing
    | otherwise = Just (mapMaybe (unificaTerm) (zip termes1 termes2))

-- Evaluacio

evaluateQueries baseConeixement queries = map (\query -> evaluateQuery baseConeixement (parseRegla query)) (map (init) (lines queries))

evaluateQuery baseConeixement query = avaluaSustitucions baseConeixement [] (_cos query)

{- Jocs de prova correctes

    huma pau.
    huma gerard.
    huma X => persona X.
    end.
    persona X => query X.
    end.

    dimoni bel.
    huma bel.
    huma X & monstre X => dimoni X.
    end.
    dimoni bel => query.
    end.

    progenitor ana brooke.
    progenitor xerces brooke.
    progenitor brooke damocles.
    end.
    progenitor X Y => query X Y.
    end.

    progenitor ana brooke.
    progenitor xerces brooke.
    progenitor brooke damocles.
    progenitor X Y => ancestre X Y.
    end.
    progenitor xerces brooke => query.
    ancestre ana brooke => query.
    end.

-}