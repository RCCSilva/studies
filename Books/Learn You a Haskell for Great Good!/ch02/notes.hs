 -- Simple List Comprehension
[x * 2 | x <- [1..10]]

-- With Checks
[x * 2 | x <- [1..10], x * 2 < 10]

-- Custom outputs based on inputs
[if x * 2 > 10 then "BOOM!" else "KABOOM!" | x <- [1..10]]

-- Two Inputs
[x * y | x <- [1, 2, 3], y <- [4, 5, 6]]

-- Custom Length
length' xs = sum [1 | _ <- xs]

-- Remove Non Upper case
removeNonUpperCase xs = [x | x <- xs, x `elem` ['A'..'Z']]

-- 
xxs = [[1,3,5,2,3,1,2,4,5],[1,2,3,4,5,6,7,8,9],[1,2,4,2,1,6,3,1,3,2,3,6]]  
[[ x | x <- xs, even x] | xs <- xxs]

-- Tuples


-- Creating Triangles
[(a, b, a^2 + b^2) | a <- [1..10], b <- [11..20]]