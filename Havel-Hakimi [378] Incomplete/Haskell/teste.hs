module Daily where
import Data.List

remove0 :: [Int] -> [Int]
remove0 [] = []
remove0 (h:t) | h == 0 = remove0 t
              | otherwise = h: (remove0 t)

isempty :: [Int] -> Bool
isempty [] = True
isempty x = False

reverseSort :: [Int] -> [Int]
reverseSort x = reverse(sort(x))

nBigger :: [Int] -> Bool
nBigger (h:t) | h > length t = False
              | otherwise = True

decList :: [Int] -> [Int]
decList [] = []
decList (h:t) = (h-1) : decList t