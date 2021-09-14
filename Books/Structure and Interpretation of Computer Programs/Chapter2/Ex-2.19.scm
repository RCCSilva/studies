(define no-more? null?)

(define except-first-denomination cdr)

(define first-denomination car) 

(define (cc amount coin-values)
    (cond ((= amount 0) 1)
    ((or (< amount 0) (no-more? coin-values)) 0)
    (else
        (+ (cc amount (except-first-denomination coin-values))
        (cc (- amount (first-denomination coin-values)) coin-values)))))

; It should not matter the order of the list since the procedure runs thought all 
; the elements of coins list.

(define us-coins (list 50 25 10 5 1))
(define us-coins-random (list 25 10 5 1 50))

(cc 100 us-coins)
(cc 100 us-coins-random)