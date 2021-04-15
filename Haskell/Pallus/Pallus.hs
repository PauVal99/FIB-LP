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
    input <- getContents
    print $ parseInput input

parseInput input = map (parseRegla) (takeWhile (/= "end.") (lines input))

parseRegla regla
    | isInfixOf regla "=>" = Regla (dropWhile (/= "=>") (words regla)) (map (parseAtom) (tail $ words atom))
    | otherwise = Regla (parseAtom regla) []

splitReglas reglas = splitOn "&" reglas

parseAtom atom = Atom (head $ words atom) (map (parseTerm) (tail $ words atom))

parseTerm term
    | isUpper $ head term = Var term
    | otherwise = Sym term