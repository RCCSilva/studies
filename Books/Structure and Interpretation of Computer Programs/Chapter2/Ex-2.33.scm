(define (accumulate op initial sequence)
    (if (null? sequence)
        initial
        (op (car sequence) (accumulate op initial (cdr sequence)))))

(define (map p sequence)
    (accumulate (lambda (a b) (cons (p a) b)) '() sequence))

(define (append seq1 seq2)
    (accumulate cons seq2 seq1))

(define (length sequence)
    (accumulate (lambda (a b) (+ 1 b)) 0 sequence))