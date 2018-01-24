
(require xrepl)

(define LIMIT 1000000)

(define problem
 (lambda ()
  (longest_collatz LIMIT)
 )
)

(define longest_collatz
 (lambda (lim)
  (- lim (index-of-max (all-collatz-len lim)))
 )
)

(define all-collatz-len
 (lambda (lim)
  (cond
   ((< lim 2) (cons (collatz-len lim) '()))
   (else (cons (collatz-len lim) (all-collatz-len (- lim 1))))
  )
 )
)

(define collatz
 (lambda (n)
  (cond
   ((eq? 1 n) '(1))
   ((even? n) (cons n (collatz (/ n 2))))
   (else (cons n (collatz (+ (* 3 n) 1))))
  )
 )
)

(define collatz-len
 (lambda (n)
  (len (collatz n))
 )
)
