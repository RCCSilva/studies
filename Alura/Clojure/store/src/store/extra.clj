(ns store.extra)

; Implements a map with tail recursion
(defn my-map [function sequence]
  (if sequence
    (do
      (let [fl (first sequence)]
        (function fl))
      (recur function (next sequence)))))

; Implements a reduce function without tail recursion
(defn my-reduce-no-tail [function sequence]
  (if (nil? (next sequence))
    (first sequence)
    (function (first sequence) (my-reduce-no-tail function (next sequence)))))


; Implements a reduce function with tail recursion
(defn my-reduce-tail [function seq]
  (let [-insider (fn [state seq]
                   (if (nil? (next seq))
                     (function state (first seq))
                     (recur (function state (first seq)) (next seq))))]
    (-insider (first seq) (next seq))))

