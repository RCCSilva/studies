data BookInfo = Book Int String [String]
                deriving (Show)

data MagazineInfo = Magazine Int String [String]
                    deriving (Show)

myInfo = Book 9780135072455 "Algebra of Programming"
         ["Richard Bird", "Oege de Moor"]

type CustomerID = Int
type ReviewBody = String


data BookReview = BetterReview BookInfo CustomerID ReviewBody

type BookRecord = (BookInfo, BookReview)


-- Payment

type CardHolder = String
type CardNumber = String
type Address = [String]

data BillingInfo = CreditCard CardNumber CardHolder Address
                    | CashOnDelivery
                    | Invoice CustomerID
                    deriving (Show)

data Customer = Customer {
    customerID :: CustomerID
    ,   customerName :: String
    ,   customerAddress :: Address
} deriving (Show)