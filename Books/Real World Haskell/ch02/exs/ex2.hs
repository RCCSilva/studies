-- 1. It needs to return a value from the list. It cannot create one or modify it.

-- 2. Create function lastButOne

lastButOne xs = if length xs == 2
                then head xs
                else lastButOne (tail xs)

-- 3. Throws an exception, since it attempts to apply the tail to an empty list