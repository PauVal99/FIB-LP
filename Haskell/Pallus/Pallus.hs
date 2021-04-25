{-# LANGUAGE RecordWildCards #-}    -- per utilitzar fields

import Data.Char (isUpper)
import Data.List (nub, isInfixOf)
import Data.List.Split (splitOn)    -- cal instal·lar: cabal install split
import Data.String.Utils (strip)    -- cal instal·lar: cabal install MissingH
import Data.Maybe (mapMaybe, fromMaybe)

type Programa = [ Regla ]
type Sustitucio = [ (Term, Term) ]
type BaseConeixement = [ Atom ]

data Regla = Regla { _cap::Atom, _cos::[ Atom ] }
    deriving (Eq, Show)
data Atom = Atom { _nomPredicat::String, _termes::[ Term ] }
    deriving (Eq, Show)
data Term = Var String | Sym String
    deriving (Eq, Show)

main = do
    programa <- getContents
    print "hola"--print $ createBaseConeixement (parsePrograma programa)
    --queries <- getContents
    --evaluateQueries baseConeixement queries

-- Helpers

getBlock block = takeWhile (/= "end") (map (init) (lines block))

-- Parser

parsePrograma :: String -> Programa
parsePrograma programa = map (parseRegla) (getBlock programa)

splitCap regla = unwords $ tail $ (dropWhile (/= "=>") (words regla))

splitCos regla = map (unwords) (splitOn ["&"] (takeWhile (/= "=>") (words regla)))

parseRegla regla
    | isInfixOf "=>" regla = Regla (parseAtom $ splitCap regla) (map (parseAtom) (splitCos regla))
    | otherwise = Regla (parseAtom regla) []

parseAtom atom = Atom (head $ words atom) (map (parseTerm) (tail $ words atom))

parseTerm term
    | isUpper $ head term = Var term
    | otherwise = Sym term

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
avaluaRegla baseConeixement regla = nub (baseConeixement ++ (sustitueix (_cap regla) (avaluaAtom baseConeixement (head $ _cos regla) []))) --falta multiples atoms

avaluaAtom :: BaseConeixement -> Atom -> [ Sustitucio ] -> [ Sustitucio ]
avaluaAtom baseConeixement atom sustitucio = mapMaybe (`unifica` atom) baseConeixement

-- Sustitucio

sustitueix :: Atom -> Sustitucio -> Atom
sustitueix atom sustitucio = Atom (_nomPredicat atom) (mapMaybe (`lookup` sustitucio) (_termes atom))

-- Unificacio

unificable (Sym terme1, Sym terme2)
    | terme1 == terme2 = True
    | otherwise = False

unificable (Var terme1, Sym terme2) = True

unificaTerm (Sym terme1, Sym terme2) = Nothing
unificaTerm (Var terme1, Sym terme2) = Just (Var terme1, Sym terme2)

uniqueSustitucio [] = True
uniqueSustitucio sustitucions = and $ map (\sustitucio -> uniqueVar sustitucio sustitucions) sustitucions  

uniqueVar (var, sym) [] = True
uniqueVar (var, sym) ((susVar, susSym):sustitucions)
    | var == susVar && sym /= susSym = False
    | otherwise = uniqueVar (var, sym) sustitucions

unifica (Atom predicat1 termes1) (Atom predicat2 termes2)
    | predicat1 /= predicat2 = Nothing
    | not $ and $ map (unificable) (zip termes1 termes2) = Nothing
    | not (uniqueSustitucio (mapMaybe (unificaTerm) (zip termes1 termes2))) = Nothing
    | otherwise = Just (mapMaybe (unificaTerm) (zip termes1 termes2))

{- Evaluator
calculateBaseConeixement programa = foldr (\baseConeixement regla -> evaluateRegla baseConeixement regla) programa  

evaluateRegla :: BaseConeixement -> Regla -> BaseConeixement
evaluateRegla baseConeixement regla
    | empty $ _cos regla = (_cap regla):baseConeixement
    | otherwise = 

evaluateQueries programa queries = map (evaluateQuery programa) (getBlock queries)

evaluateQuery programa query = calculateBaseConeixement programa

evaluateRegla programa query = 


avaluaAtom :: BaseConeixement -> Atom -> [ Sustitucio ] -> [ Sustitucio ]
unifica :: Atom -> Atom -> Maybe Sustitucio
sustitueix :: Atom -> Sustitucio -> Atom
sustitucioBuida :: Sustitucio
sustitucioBuida = []

sustitueix :: Atom -> Sustitucio -> Atom
sustitueix (ancestre X Y) [ (X, ana), (Y, brooke)] -> ancestre ana brooke

avaluaAtom :: BaseConeixement -> Atom -> [ Sustitucio ] -> [ Sustitucio ]
avaluaAtom [progenitor ana brooke, progenitor xerces brooke, progenitor brooke damocles] (progenitor X Y) [[]] -> [[(X, ana), (Y, brooke)], [(X, xerces), (Y, brooke)], [(X, brooke), (Y, damocles)]]
-}