(ns store.core
  (:require [store.db :as db]))

(defn get-item-unity-price
  [[name details]]
  (* (get details :quantity 0) (get details :unity-price 0)))

(defn user-total-spent
  [[user orders]]
  {
   :user        user
   :orders      (count orders)
   :total-spent (->> orders (map (comp vals :items)) flatten (map :unity-price) (reduce +))
   })

(->> db/all-orders
     (group-by :user)
     (map user-total-spent)
     (println))
