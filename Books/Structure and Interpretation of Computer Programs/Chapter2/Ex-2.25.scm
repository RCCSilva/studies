'(1 3 (5 7) 9) ; cdr cdr car car cdr

(car (cdr (car (cdr (cdr '(1 3 (5 7) 9))))))
;;

((7))

(car (car '((7)) ))

;;

(define x '(1 (2 (3 (4 (5 (6 7)))))))

;; The scheme if the data was organized from directly from pairs

  /  \
  1 /  \
    2 /  \
      3 /  \
        4 /  \
          5 /  \
            6  7

;; However, the data was built on top of lists. Thus, when we call the procedure `cdr` on the list
;; we actually get a list of all the values (null included) except the first. That is why when we can't
;; just use 5 `cdr` on this problem. We need to call `car` as well to take the first value of the returned list.

;; 5 pairs of (car (cdr )):
(car (cdr (car (cdr (car (cdr (car (cdr (car (cdr (car (cdr x))))))))))))