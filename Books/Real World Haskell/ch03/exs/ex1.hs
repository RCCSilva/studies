
-- Ex 1

data List a = Cons a (List a)
            | Nil
            deriving (Show)

toList (Cons x xs) = x : (toList xs)
toList Nil = []

-- Ex 2
data Tree a = Node a (Maybe (Tree a)) (Maybe (Tree a))
            deriving (Show)