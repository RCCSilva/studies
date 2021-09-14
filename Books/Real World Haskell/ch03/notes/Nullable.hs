data Maybe a = Just a | Nothing

data List a = Cons a (List a) | Nil deriving (Show)