
(define len
 (lambda (lis)
    (if (null? lis) 0 (+ 1 (len (cdr lis))))
 )
)

(define index-of-max
 (lambda (lis)
  (index-of-max-sub lis 0 0 0)
 )
)

(define index-of-max-sub
 (lambda (lis cur-idx max-idx max-val)
  (cond
   ((null? lis)
    max-idx
   )
   ((> (car lis) max-val)
    (index-of-max-sub (cdr lis) (+ cur-idx 1) cur-idx (car lis))
   )
   (else
    (index-of-max-sub (cdr lis) (+ cur-idx 1) max-idx max-val)
   )
  )
 )
)
