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

parseInput input = map (parseRegla) (takeWhile (/= "end") (map (init) (lines input)))

splitCap regla = unwords $ tail $ (dropWhile (/= "=>") (words regla))

splitCos regla = map (unwords) (splitOn ["&"] (takeWhile (/= "=>") (words regla)))

parseRegla regla
    | isInfixOf "=>" regla = Regla (parseAtom $ splitCap regla) (map (parseAtom) (splitCos regla))
    | otherwise = Regla (parseAtom regla) []

parseAtom atom = Atom (head $ words atom) (map (parseTerm) (tail $ words atom))

parseTerm term
    | isUpper $ head term = Var term
    | otherwise = Sym term