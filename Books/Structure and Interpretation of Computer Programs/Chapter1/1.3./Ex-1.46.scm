(define (fixed-point good-enougth improve)
    (define (try guess)
        (let ((next (improve guess)))
            (if (close-enough? guess next)
                guess
                (try next))))

    (lambda (guess) (try guess)))