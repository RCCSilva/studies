(ns store.db)

(def order-1 {
              :user  15
              :items {:backpack {:quantity 2 :unity-price 80}
                      :t-shit   {:quantity 10 :unity-price 100}
                      }
              })

(def order-2 {
              :user  15
              :items {:backpack {:quantity 10 :unity-price 30}
                      :t-shit   {:quantity 1 :unity-price 1}
                      }
              })

(def order-3 {
              :user  1
              :items {:backpack {:quantity 2 :unity-price 80}
                      :t-shit   {:quantity 10 :unity-price 100}
                      }
              })

(def all-orders
  [order-1 order-2 order-3])